# scheduler.py
# This file sets up and manages background scheduled tasks.
# It uses the APScheduler library to schedule tasks such as the daily web scraping and email sending job.
# The scheduler is started on application startup, ensuring background jobs run as specified.

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.handlers.user_handler import get_user_by_id
from app.utils.scraper import download_enrollment_file
from app.utils.emailer import send_email_with_attachment

scheduler = AsyncIOScheduler()

@scheduler.scheduled_job("interval", hours=24)
async def scheduled_task():
    user_data = await get_user_by_id(user_id) # type: ignore
    pdf_path = await download_enrollment_file(user_data.username, user_data.password)
    if pdf_path:
        send_email_with_attachment(user_data.email, user_data, pdf_path)
