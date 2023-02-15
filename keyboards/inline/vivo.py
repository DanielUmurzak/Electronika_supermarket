from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

vivo_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Vivo Y02, 2/32 ГБ", callback_data="y02_callback")
        ],
        [
            InlineKeyboardButton(text="vivo V25e, 8/128 ГБ", callback_data="v25_callback")
        ],
        [
            InlineKeyboardButton(text="vivo Y22, 4/64 ГБ", callback_data="y22_callback")
        ],
        [
            InlineKeyboardButton(text=" Vivo Y15S, 3/32GB", callback_data="y15s_callback")
        ],
        [
            InlineKeyboardButton(text="vivo Y53s, 8/128 ГБ", callback_data="y53_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="vivo_page")
        ]
    ]
)

back_to_vivo_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="vivo_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)
