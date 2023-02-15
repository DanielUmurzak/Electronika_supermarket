from keyboards.inline.pocco import poco_button, back_to_poco_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="poco_callback")
@dp.callback_query_handler(text="Pocco_callback")
async def Pocco_callback_func(call: CallbackQuery):
    text = "Smartfonlardan birini tanlang"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/poco.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="x4_callback")
async def x4_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO X4 GT.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="x4_callback")
async def x4_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO X4 GT.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="c40_callback")
async def c40_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO X4 Pro 5G.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="m4_callback")
async def m4_callback(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO M4 Pro.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="f4_callback")
async def f4_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO F4 GT.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()


@dp.callback_query_handler(text="x4_pro_callback")
async def x4_pro_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/poco/POCO X4 Pro 5G.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_poco_button)
    await call.message.delete()
