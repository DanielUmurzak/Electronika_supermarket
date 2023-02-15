from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


xolodilnik_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Roison RHWG DF2-27 W/S", callback_data="roison_callback")
        ],
        [
            InlineKeyboardButton(text="Atlant ХМ-4421-000-N", callback_data="atlant_callback")
        ],
        [
            InlineKeyboardButton(text="TCL Invertor Total No Frost", callback_data="tcl_callback")
        ],
        [
            InlineKeyboardButton(text="BEKO CNKL7321EC0S", callback_data="beko_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_maishiy")
        ],
    ]
)


backto_fridge = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="muzlatgich_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]

    ]
)
