from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

redmi_list = ["Xiaomi 12 Lite 6/128GB Lite Black", "Xiaomi Redmi Note 11 Pro 8/128GB ", "Xiaomi Redmi A1+, 2/32 ГБ",
              "Xiaomi Redmi 10 6/128 GB", "Xiaomi Redmi 10C 3/64GB"]
redmi_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xiaomi 12 Lite 6/128GB ", callback_data="xiaomi_12_callback")
        ],
        [
            InlineKeyboardButton(text="Xiaomi Redmi Note 11 Pro 8/128GB ", callback_data="pro_11_callback")
        ],
        [
            InlineKeyboardButton(text="Xiaomi Redmi A1+, 2/32 ГБ", callback_data="a1_callback")
        ],
        [
            InlineKeyboardButton(text="Xiaomi Redmi 10 6/128 GB", callback_data="redmi_10_callback")
        ],
        [
            InlineKeyboardButton(text="Xiaomi Redmi 10C 3/64GB", callback_data="redmi_10c_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="samsung_page")
        ]
    ]
)
