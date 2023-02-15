from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


samsung_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Samsung Galaxy Book Pro 15 360 (i7-1165G7)", callback_data="pro_15_360_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy Book Pro 15 (i5-1135G7)", callback_data="pro_15_i5_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy Book Flex2", callback_data="flex_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy Book Pro 360 13 (i7-1165G7)", callback_data="pro_360_13_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_laptop")
        ],
    ]
)

back_laptops = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="samsung_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

