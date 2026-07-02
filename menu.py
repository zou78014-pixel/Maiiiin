from telegram import Update
from telegram.ext import ContextTypes

from handlers.azkar import azkar
from handlers.quran import quran


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📿 الأذكار":
        await azkar(update, context)

    elif text == "📖 القرآن الكريم":
        await quran(update, context)

    elif text == "⚙️ الإعدادات":
        await update.message.reply_text("⚙️ صفحة الإعدادات.")

    elif text == "ℹ️ حول البوت":
        await update.message.reply_text(
            "🤲 بوت القرآن والأذكار\n\nالإصدار: 1.0"
        )