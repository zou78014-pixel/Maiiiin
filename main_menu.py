from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ["🕌 مواقيت الصلاة", "📿 الأذكار"],
        ["📖 القرآن الكريم", "⚙️ الإعدادات"],
        ["ℹ️ حول البوت"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )