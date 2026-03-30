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
    from datetime import datetime, timedelta

async def test_message():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Test thành công! Bot đang hoạt động."
    )

# Chạy sau 60 giây
run_time = datetime.now() + timedelta(seconds=60)
scheduler.add_job(test_message, 'date', run_date=run_time)

    scheduler.add_job(send_tuesday, 'cron', day_of_week='tue', hour=11, minute=30)
    scheduler.add_job(send_friday, 'cron', day_of_week='fri', hour=16, minute=30)

    scheduler.start()
    print("Bot đang chạy trên server...")

    while True:
        await asyncio.sleep(60)

asyncio.run(main())
