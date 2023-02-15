from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


microvawe_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="BEKO MOC20100S", callback_data="beko_moc20100s_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung ME 81 ARW White", callback_data="samsung_me_81_callback")
        ],
        [
            InlineKeyboardButton(text="Goodwell GMF 2301 BL", callback_data="goodwell_gmf_callback")
        ],
        [
            InlineKeyboardButton(text="Hofmann HMW-720SS 20 л", callback_data="hofman_hmw_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_maishiy")
        ],
    ]
)


microvawe_washing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="microwave_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]

    ]
)
