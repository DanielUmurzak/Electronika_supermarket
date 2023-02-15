from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True)
        ]
    ], resize_keyboard=True
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location", request_location=True)
        ]
    ], resize_keyboard=True
)

res_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
    ], resize_keyboard=True
)