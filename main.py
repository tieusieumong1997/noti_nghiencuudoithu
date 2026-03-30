import asyncio
import pytz
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

# =============================
# THÔNG TIN BOT
# =============================
TOKEN = "8613307205:AAGFEeBedkeb_Yy5_Fnx5JQSVs3ScNqr5Vg"
CHAT_ID = -1002672769813

bot = Bot(token=TOKEN)

# =============================
# HÀM GỬI TIN NHẮN CHÍNH
# =============================
async def send_message():
    try:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="mọi người điền file nghiên cứu đối thủ"
        )
        print("✅ Đã gửi tin nhắn lúc:", datetime.now())
    except Exception as e:
        print("❌ Lỗi khi gửi tin:", e)

# =============================
# HÀM TEST KHI KHỞI ĐỘNG
# =============================
async def startup_test():
    try:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🚀 Bot đã khởi động thành công!"
        )
        print("✅ Gửi test thành công")
    except Exception as e:
        print("❌ Lỗi test:", e)

# =============================
# MAIN
# =============================
async def main():
    timezone = pytz.timezone("Asia/Ho_Chi_Minh")
    scheduler = AsyncIOScheduler(timezone=timezone)

    # 🔹 Thứ 3 - 11:00
    scheduler.add_job(
        send_message,
        trigger="cron",
        day_of_week="tue",
        hour=11,
        minute=0
    )

    # 🔹 Thứ 6 - 16:30
    scheduler.add_job(
        send_message,
        trigger="cron",
        day_of_week="fri",
        hour=16,
        minute=30
    )

    scheduler.start()
    print("🤖 Bot đang chạy...")

    # Gửi tin test khi khởi động
    await startup_test()

    # Giữ bot chạy liên tục trên Railway
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
