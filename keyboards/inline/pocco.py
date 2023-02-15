from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

poco_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="POCO X4 GT", callback_data="x4_callback")
        ],
        [
            InlineKeyboardButton(text="POCO C40", callback_data="c40_callback")
        ],
        [
            InlineKeyboardButton(text="POCO M4 Pro", callback_data="m4_callback")
        ],
        [
            InlineKeyboardButton(text="POCO F4 GT", callback_data="f4_callback")
        ],
        [
            InlineKeyboardButton(text="POCO X4 Pro 5G", callback_data="x4_pro_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="samsung_page")
        ]
    ]
)

back_to_poco_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="poco_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)
