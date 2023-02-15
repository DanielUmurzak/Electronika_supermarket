from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


maishiy_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Muzlatgich", callback_data="muzlatgich_callback")
        ],
        [
            InlineKeyboardButton(text="Kir yuvish mashinasi", callback_data="washing_machin_callback")
        ],
        [
            InlineKeyboardButton(text="Micravalnovka", callback_data="microwave_callback")
        ],
        [
            InlineKeyboardButton(text="Gaz plita", callback_data="gaz_plita_callback")
        ],
        [
            InlineKeyboardButton(text="↩️ Ortga", callback_data="back_to_menu")
        ],
    ]
)

