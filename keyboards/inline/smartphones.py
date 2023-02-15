from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

phone_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Samsung", callback_data="Samsung_callback")
        ],
        [
            InlineKeyboardButton(text="Apple", callback_data="Apple_callback")
        ],
        [
            InlineKeyboardButton(text="RedMi", callback_data="RedMi_callback")
        ],
        [
            InlineKeyboardButton(text="Poco", callback_data="Pocco_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_menu"),
            InlineKeyboardButton(text="⏩ Keyingi bet", callback_data="phone_next_page")

        ]
    ]
)

phone_button_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Vivo", callback_data="Vivo_callback")
        ],
        [
            InlineKeyboardButton(text="Huwavei", callback_data="Huwavei_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_page_phone_1")
        ]
    ]
)

Samsung_callback_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Samsung Galaxy S22 Ultra", callback_data="ultra_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy A53", callback_data="a53_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy Z Fold 4", callback_data="z_fold_4_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy S21 FE", callback_data="s21_callback")
        ],
        [
            InlineKeyboardButton(text="Samsung Galaxy Z Flip 4", callback_data="z_flip_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="samsung_page")
        ]
    ]
)

back_to_samsung_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="Samsung_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

back_to_iphone_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="iphone_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

back_to_redmi_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="redmi_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)

back_to_phones_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="Apple_callback")
        ]
    ]
)

