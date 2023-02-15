from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

acer_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ACER ASPIRE 3 A315", callback_data="aspire_callback")
        ],
        [
            InlineKeyboardButton(text="Acer S5-371T", callback_data="s5_callback")
        ],
        [
            InlineKeyboardButton(text="Acer Swift 3 SF314-511", callback_data="swift_callback")
        ],
        [
            InlineKeyboardButton(text="Acer EX215-52", callback_data="ex215_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_laptop")
        ],
    ]
)

back_laptops = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="acer_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)
