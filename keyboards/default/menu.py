from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Smartfonlar"),
            KeyboardButton(text="💻 Noutbooklar")
        ],

        [
            KeyboardButton(text="🔌 Maishiy texnika")
        ],
    ],
    resize_keyboard=True
)
