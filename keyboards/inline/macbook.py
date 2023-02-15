from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


macbook_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="MacBook Pro 16-inch(M2)", callback_data="pro_16_m2_callback")
        ],
        [
            InlineKeyboardButton(text="MacBook Pro 14-inch(M2)", callback_data="pro_14_m2_callback")
        ],
        [
            InlineKeyboardButton(text="MacBook Pro 16-inch(M1)", callback_data="pro_16_m1_callback")
        ],
        [
            InlineKeyboardButton(text="MacBook Pro 14-inch(M1)", callback_data="pro_14_m1_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_laptop")
        ],
    ]
)

back_laptops = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="macbook_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

