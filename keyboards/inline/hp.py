from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


hp_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Victus 16-E0156UR R7-5800H", callback_data="victus_callback")
        ],
        [
            InlineKeyboardButton(text="Pavilion 15-EH1067UR R5-5500U", callback_data="pavilion_callback")
        ],
        [
            InlineKeyboardButton(text="hp 15S-FQ3043UR N4500", callback_data="s15_callback")
        ],
        [
            InlineKeyboardButton(text="Pavilion X360 Convertible", callback_data="x360_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_laptop")
        ],
    ]
)

back_laptops = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="hp_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

