from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

huawei_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" Huawei Nova Y70 4/64GB", callback_data="y70_callback")
        ],
        [
            InlineKeyboardButton(text="Huawei Nova 9 SE 8/128 GB", callback_data="se9_callback")
        ],
        [
            InlineKeyboardButton(text="Huawei Nova Y90 4/128 GB", callback_data="y90_callback")
        ],
        [
            InlineKeyboardButton(text="Huawei Honor 80 SE", callback_data="se80_callback")
        ],
        [
            InlineKeyboardButton(text="Huawei Nova Y61", callback_data="y61_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="vivo_page")
        ]
    ]
)

back_to_huawei_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="huawei_callback"),
            InlineKeyboardButton(text="🛒 Savatga solish", callback_data="buy_item"),
            InlineKeyboardButton(text="Bosh menyu", callback_data="bosh_menu")
        ]
    ]
)
