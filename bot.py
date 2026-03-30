import asyncio
import os
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_tuesday():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="📢 11h30 Thứ 3 - Nhắc điền báo cáo tuần!"
    )

async def send_friday():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="📊 16h30 Thứ 6 - Kiểm tra & tổng kết báo cáo!"
    )

async def main():
    scheduler = AsyncIOScheduler(timezone="Asia/Ho_Chi_Minh")

    scheduler.add_job(send_tuesday, 'cron', day_of_week='tue', hour=11, minute=30)
    scheduler.add_job(send_friday, 'cron', day_of_week='fri', hour=16, minute=30)

    scheduler.start()
    print("Bot đang chạy trên server...")

    while True:
        await asyncio.sleep(60)

asyncio.run(main())
