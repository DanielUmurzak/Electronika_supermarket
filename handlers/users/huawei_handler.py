from keyboards.inline.huawei import huawei_button, back_to_huawei_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="huawei_callback")
@dp.callback_query_handler(text="Huwavei_callback")
async def huawei_callback_func(call: CallbackQuery):
    text = "Smartfonlardan birini tanlang"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/huawei.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="y70_callback")
async def y70_callback_func(call: CallbackQuery):
    text = '🔻Процессор: HiSilicon Kirin 710A, 8 ядер, 2.2 ГГц\n' \
           '🔻Оперативная память: 4 ГБ\n' \
           '🔻Встроенная память: 64 ГБ\n' \
           '🔻Основные камеры: 48 МП + 5 МП + 2 МП\n' \
           '🔻Eмкость аккумулятора: 6000 мА/ч\n' \
           '🔻Вес: 199 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/Huawei Nova Y70.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="se9_callback")
async def se9_callback(call: CallbackQuery):
    text = '🔻Процессор: HiSilicon Kirin 710A, 8 ядер, 2.2 ГГц\n' \
           '🔻Оперативная память: 4 ГБ\n' \
           '🔻Встроенная память: 64 ГБ\n' \
           '🔻Основные камеры: 48 МП + 5 МП + 2 МП\n' \
           '🔻Eмкость аккумулятора: 6000 мА/ч\n' \
           '🔻Вес: 199 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/Huawei Nova 9 SE.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="y90_callback")
async def y90_callback_func(call: CallbackQuery):
    text = '🔻Процессор: HiSilicon Kirin 710A, 8 ядер, 2.2 ГГц\n' \
           '🔻Оперативная память: 4 ГБ\n' \
           '🔻Встроенная память: 64 ГБ\n' \
           '🔻Основные камеры: 48 МП + 5 МП + 2 МП\n' \
           '🔻Eмкость аккумулятора: 6000 мА/ч\n' \
           '🔻Вес: 199 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/Huawei Nova Y90.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="se80_callback")
async def se80_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.67" OLED - 1080 x 2400\n' \
           '🔻Чип: MediaTek Dimensity 900\n' \
           '🔻Камера: 3 (64 MP + 5 MP + 2 MP\n' \
           '🔻Батарея: 4600 мАч\n' \
           '🔻OS: Android 12\n' \
           '🔻Вес: 175 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/honor_80_se_black.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="se80_callback")
async def se80_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.67" OLED - 1080 x 2400\n' \
           '🔻Чип: MediaTek Dimensity 900\n' \
           '🔻Камера: 3 (64 MP + 5 MP + 2 MP\n' \
           '🔻Батарея: 4600 мАч\n' \
           '🔻OS: Android 12\n' \
           '🔻Вес: 175 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/honor_80_se_black.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()


@dp.callback_query_handler(text="y61_callback")
async def y61_callback_func(call: CallbackQuery):
    text = '🔻Дисплей: 6.52" IPS LCD - 720 x 1600\n' \
           '🔻Чип: HiSilicon Kirin 710A\n' \
           '🔻Камера: 3 (50 MP + 2 MP + 2 MP)\n' \
           '🔻Батарея: 5000 мАч\n' \
           '🔻OS: Android 12\n' \
           '🔻Вес: 188 г.'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/huawei/Huawei Nova Y61.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_huawei_button)
    await call.message.delete()
