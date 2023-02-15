from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


gaz_plita_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gefest ПГ 6100-02 0309", callback_data="gefest_pg_callback")
        ],
        [
            InlineKeyboardButton(text="Artel Apetito, 02-G CHU ГП", callback_data="artel_apetito_callback")
        ],
        [
            InlineKeyboardButton(text="Бирюса U60GG12SS", callback_data="biryusa_u60gg12ss_callback")
        ],
        [
            InlineKeyboardButton(text="Бирюса U90GG90SS", callback_data="biryusa_u90gg90ss_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_maishiy")
        ],
    ]
)


back_to_gaz_plita = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="gaz_plita_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]

    ]
)
