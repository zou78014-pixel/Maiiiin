from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.main_menu import main_menu


async def azkar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🌅 أذكار الصباح"],
        ["🌙 أذكار المساء"],
        ["🤲 أذكار بعد الصلاة"],
        ["⬅️ رجوع"]
    ]

    await update.message.reply_text(
        "📿 اختر نوع الأذكار:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def azkar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🌅 أذكار الصباح":
        await update.message.reply_text(
"""🌅 أذكار الصباح

📿 اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور.

📿 أصبحنا وأصبح الملك لله رب العالمين.

📿 سبحان الله وبحمده ×100

📿 لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير ×100

📿 أستغفر الله وأتوب إليه."""
        )

    elif text == "🌙 أذكار المساء":
        await update.message.reply_text(
"""🌙 أذكار المساء

📿 اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت وإليك المصير.

📿 أمسينا وأمسى الملك لله رب العالمين.

📿 سبحان الله وبحمده ×100

📿 لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير ×100

📿 أستغفر الله وأتوب إليه."""
        )

    elif text == "🤲 أذكار بعد الصلاة":
        await update.message.reply_text(
"""🤲 أذكار بعد الصلاة

📿 أستغفر الله ×3

📿 اللهم أنت السلام ومنك السلام تباركت يا ذا الجلال والإكرام.

📿 سبحان الله ×33

📿 الحمد لله ×33

📿 الله أكبر ×34

📿 لا إله إلا الله وحده لا شريك له، له الملك وله اkلحمد وهو على كل شيء قدير."""
        )

    elif text == "⬅️ رجوع":
        await update.message.reply_text(
            "🏠 القائمة الرئيسية",
            reply_markup=main_menu()
        )