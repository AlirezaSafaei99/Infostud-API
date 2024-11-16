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
from app.models import User
from app.database import init_db
from config.config import load_config
import os
import requests

config = load_config()
urls = config["urls"]

def initialize_driver():
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
            return user.info_user, user.pass_user
        else:
            raise Exception(f"User with ID {user_id} not found.")

async def download_enrollment_file(user_id: int):
    username, password = await get_user_credentials(user_id)

    driver = initialize_driver()
    wait =  WebDriverWait(driver, 10)

    try:
        # Go to the login page
        driver.get(urls["homepage"])

        # Log into the user account
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

