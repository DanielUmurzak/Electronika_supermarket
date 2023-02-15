from aiogram.dispatcher import FSMContext
from keyboards.default.contact_info import location_button, contact_button
from keyboards.default.menu import menu_button
from keyboards.inline.smartphones import phone_button, phone_button_2, Samsung_callback_button, back_to_phones_button, \
    back_to_samsung_button
from loader import dp
from aiogram.types import Message, CallbackQuery
from states.personal_info import PersonalData


@dp.message_handler(text="📱 Smartfonlar")
async def phone_button_func(msg: Message):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/smartphones.jpg", "rb")
    await msg.answer_photo(pic, text, reply_markup=phone_button)


@dp.callback_query_handler(text="samsung_page")
async def phone_button_func(call: CallbackQuery):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/smartphones.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=phone_button)
    await call.message.delete()


@dp.callback_query_handler(text="vivo_page")
@dp.callback_query_handler(text="phone_next_page")
async def phone_next_page_func(call: CallbackQuery):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/smartphones.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=phone_button_2)
    await call.message.delete()


@dp.callback_query_handler(text="back_to_menu")
async def back_to_menu_func(call: CallbackQuery):
    await call.message.answer(f"Salom !", reply_markup=menu_button)
    await call.message.delete()


@dp.callback_query_handler(text="back_to_page_phone_1")
async def back_to_page_phone_1_func(call: CallbackQuery):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/smartphones.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=phone_button)
    await call.message.delete()


"""Samsung part"""


@dp.callback_query_handler(text="Samsung_callback")
async def Samsung_callback_func(call: CallbackQuery):
    text = "Smartfonlardan birini tanlang"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=Samsung_callback_button)
    await call.message.delete()


@dp.callback_query_handler(text="ultra_callback")
async def ultra_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.8" Dynamic AMOLED - 1440 x 3088\n' \
           '🔻Чип: Samsung Exynos 2200\n' \
           '🔻Камера: 4 (108 MP + 10 MP + 10 MP + 12 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13 \n' \
           '🔻Вес: 228 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung/s22_ultra.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_samsung_button)
    await call.message.delete()


@dp.callback_query_handler(text="a53_callback")
async def a53_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.5" Super AMOLED - 1080 x 2400\n' \
           '🔻Чип: Samsung Exynos 1280\n' \
           '🔻Камера: 4 (64 MP + 12 MP + 5 MP + 5 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 13\n' \
           '🔻Вес: 189 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung/a53.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_samsung_button)
    await call.message.delete()


@dp.callback_query_handler(text="z_fold_4_callback")
async def z_fold_4_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 7.6" Dynamic AMOLED - 1812 x 2176\n' \
           '🔻Чип: Qualcomm Snapdragon 8 Plus Gen 1\n' \
           '🔻Камера: 3 (50 MP + 12 MP + 12 MP)\n' \
           '🔻Батарея: 4400 мАч\n' \
           '🔻OS: Android 13\n' \
           '🔻Вес: 263 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung/z_fold_4.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_samsung_button)
    await call.message.delete()


@dp.callback_query_handler(text="s21_callback")
async def s21_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.4" Dynamic AMOLED - 1080 x 2340\n' \
           '🔻Чип: Qualcomm Snapdragon 888\n' \
           '🔻Камера: 3 (12 MP + 8 MP + 12 MP)\n' \
           '🔻Батарея: 4500 мАч\n' \
           '🔻OS: Android 13\n' \
           '🔻Вес: 177 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung/s21.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_samsung_button)
    await call.message.delete()


@dp.callback_query_handler(text="z_flip_callback")
async def z_flip_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.7" Dynamic AMOLED - 1080 x 2640\n' \
           '🔻Чип: Qualcomm Snapdragon 8 Plus Gen 1\n' \
           '🔻Камера: 2 (12 MP + 12 MP)\n' \
           '🔻Батарея: 3700 мАч\n' \
           '🔻OS: Android 13\n' \
           '🔻Вес: 187 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung/Z Flip 4.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_samsung_button)
    await call.message.delete()


