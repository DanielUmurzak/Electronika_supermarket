from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


iphone_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="iPhone 14 Pro Max", callback_data="promax_callback")
        ],
        [
            InlineKeyboardButton(text="iPhone 14 Pro", callback_data="pro_callback")
        ],
        [
            InlineKeyboardButton(text="iPhone 14 Plus", callback_data="plus_callback")
        ],
        [
            InlineKeyboardButton(text="iPhone 14", callback_data="i14_callback")
        ],
        [
            InlineKeyboardButton(text="iPhone SE (3-го поколения)", callback_data="se_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="samsung_page")
        ]
    ]
)
