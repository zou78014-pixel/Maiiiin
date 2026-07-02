import requests

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters
from database import save_city
CITY = 1


async def prayers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 أرسل اسم مدينتك.\n\nمثال:\nAlgiers\nOran\nConstantine"
    )
    return CITY


async def get_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    save_city(update.effective_user.id, city)
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Algeria&method=3"

    try:
        data = requests.get(url).json()
        timings = data["data"]["timings"]

        await update.message.reply_text(
            f"""🕌 مواقيت الصلاة في {city}

🌅 الفجر : {timings['Fajr']}
☀️ الشروق : {timings['Sunrise']}
🕛 الظهر : {timings['Dhuhr']}
🌇 العصر : {timings['Asr']}
🌆 المغرب : {timings['Maghrib']}
🌙 العشاء : {timings['Isha']}"""
        )

    except:
        await update.message.reply_text("❌ المدينة غير موجودة.")

    return ConversationHandler.END