from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

laptop_button = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Acer", callback_data="acer_callback")
        ],
        [
            InlineKeyboardButton(text="HP", callback_data="hp_callback")
        ],
        [
            InlineKeyboardButton(text="Macbook", callback_data="macbook_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung", callback_data="samsung_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_menu"),
        ]
    ]
)
