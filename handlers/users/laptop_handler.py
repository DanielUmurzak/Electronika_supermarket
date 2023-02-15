from keyboards.inline.laptops import laptop_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.message_handler(text="💻 Noutbooklar")
async def noutbooklar_func(msg: Message):
    text = "Noutbuklar"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/best-laptop-medium.jpg", "rb")
    await msg.answer_photo(pic, text, reply_markup=laptop_button)


@dp.callback_query_handler(text="back_to_laptop")
async def back_to_laptop_func(call: CallbackQuery):
    text = "Noutbuklar"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/best-laptop-medium.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=laptop_button)
