from telegram import Update
from telegram.ext import ContextTypes
from keyboards.main_menu import main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕌 السلام عليكم ورحمة الله وبركاته\n\n"
        "أهلاً بك في بوت القرآن والأذكار.",
        reply_markup=main_menu()
    )