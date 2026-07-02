import json
import requests

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.main_menu import main_menu


def load_surahs():
    with open("data/surahs.json", "r", encoding="utf-8-sig") as f:
        return json.load(f)


async def quran(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📚 فهرس السور"],
        ["📖 سورة اليوم"],
        ["⬅️ رجوع"]
    ]

    await update.message.reply_text(
        "📖 القرآن الكريم\n\nاختر أحد الخيارات:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def quran_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 فهرس السور":
        try:
            surahs = load_surahs()

            message = "📚 فهرس سور القرآن الكريم\n\n"

            for surah in surahs:
                message += f"{surah['id']}. {surah['name']}\n"

            message += "\n\n✍️ أرسل رقم السورة (من 1 إلى 114)."

            await update.message.reply_text(message)

        except Exception as e:
            await update.message.reply_text(f"❌ حدث خطأ:\n{e}")

    elif text == "📖 سورة اليوم":
        await update.message.reply_text(
            "📖 سورة اليوم: الفاتحة\n\nأرسل رقم أي سورة لقراءتها."
        )

    elif text == "⬅️ رجوع":
        await update.message.reply_text(
            "🏠 القائمة الرئيسية",
            reply_markup=main_menu()
        )


async def read_surah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.isdigit():
        return

    number = int(text)

    if number < 1 or number > 114:
        await update.message.reply_text("❌ رقم السورة يجب أن يكون بين 1 و114.")
        return

    try:
        url = f"https://api.alquran.cloud/v1/surah/{number}"

        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            await update.message.reply_text("❌ تعذر جلب السورة.")
            return

        data = response.json()["data"]

        message = f"📖 سورة {data['name']}\n\n"

        for aya in data["ayahs"]:
            line = f"{aya['text']} ({aya['numberInSurah']})\n"

            if len(message) + len(line) > 4000:
                await update.message.reply_text(message)
                message = ""

            message += line

        if message:
            await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"❌ حدث خطأ:\n{e}")