from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


washing_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" TCL Invertor Combo", callback_data="tcl_combo_callback")
        ],
        [
            InlineKeyboardButton(text="Bosch WGA242X0ME", callback_data="bosch_callback")
        ],
        [
            InlineKeyboardButton(text="BEKO WSPE6H616S", callback_data="beko_wspe_callback")
        ],
        [
            InlineKeyboardButton(text="Haier HWD80-BP14979S", callback_data="haier_hwd_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_maishiy")
        ],
    ]
)


backto_washing = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="washing_machin_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]

    ]
)
