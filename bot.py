import asyncio
import os
from datetime import datetime, timedelta
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_tuesday():
    await bot.send_message(chat_id=CHAT_ID, text="Thông báo thứ 3!")

async def send_friday():
    await bot.send_message(chat_id=CHAT_ID, text="Thông báo thứ 6!")

async def test_message():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Test thành công! Bot đang hoạt động."
    )

async def main():
    scheduler = AsyncIOScheduler(timezone="Asia/Ho_Chi_Minh")

    # 🔥 Test sau 60 giây
    run_time = datetime.now() + timedelta(seconds=60)
    scheduler.add_job(test_message, 'date', run_date=run_time)

    # Lịch chính
    scheduler.add_job(send_tuesday, 'cron', day_of_week='tue', hour=11, minute=30)
    scheduler.add_job(send_friday, 'cron', day_of_week='fri', hour=16, minute=30)

    scheduler.start()
    print("Bot đang chạy trên server...")

    while True:
        await asyncio.sleep(60)

asyncio.run(main())
