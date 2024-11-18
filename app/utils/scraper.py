# scraper.py
# This file contains functions for web scraping using Selenium.
# It defines functions to log in to the university website, download enrollment files, and save them.
# The scraper is scheduled to run daily and authenticate using user credentials stored in the database.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, EnrollmentFile
from app.database import init_db
from config.config import load_config
import os
import requests
import datetime

config = load_config()
urls = config["urls"]

def initialize_driver():
    """Initialize the Selenium WebDriver with headless options."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver

async def get_user_credentials(user_id: int):
    async_session = init_db
    async with async_session as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalars().first()
        if user:
            return user
        else:
            raise Exception(f"User with ID {user_id} not found.")

async def save_pdf_to_db(user_id: int, pdf_path: str):
    """
    Save the downloaded PDF file to the database.

    Parameters:
        user_id (int): ID of the user associated with the file.
        pdf_path (str): Local path of the downloaded file.
    """
    async_session = init_db()
    async with async_session() as session:
        with open(pdf_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()

        enrollment_file = EnrollmentFile(
            user_id=user_id,
            file_path=pdf_path,
            pdf_data=pdf_data,
            uploaded_at=datetime.datetime.now().isformat()
        )

        session.add(enrollment_file)
        await session.commit()

async def download_enrollment_file(user_id: int):
    """
    Download the enrollment file for a user and store it in the database.

    Parameters:
        user_id (int): ID of the user to fetch credentials and download the file.
    """
    user = await get_user_credentials(user_id)
    username, password = user.info_user, user.pass_user

    driver = initialize_driver()
    wait =  WebDriverWait(driver, 10)

    try:
        # Go to the login page
        driver.get(urls["homepage"])

        # Navigate to the login button and click it
        desktop_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktop")))
        desktop_button.click()

        # Log into the user account
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Navigate to "CORSI DI LAUREA"
        corsi_di_laurea = wait.until(EC.element_to_be_clickable((By.LINK_TETX,"CORSI DI LAUREA")))
        corsi_di_laurea.clock()

        # Select "CERTIFICATI"
        certificati = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CERTIFICATI")))
        certificati.click()

        # Select "ISCRIZIONE ENG" and download the PDF
        iscrizione_eng = wait.until(EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "ISCRIZIONE ENG")]')))
        iscrizione_eng.click()

        # Click "STAMPA" to download the file
        stampa_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "STAMPA")]')))
        stampa_button.click()

        pdf_filename = f"{user.info_user}_enrollment.pdf"
        pdf_path = os.path.join("downloads", pdf_filename)
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        await save_pdf_to_db(user_id, pdf_path)
        return pdf_path

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

