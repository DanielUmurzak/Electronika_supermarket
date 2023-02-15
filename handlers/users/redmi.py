from keyboards.default.menu import menu_button
from keyboards.inline.redmi import redmi_button
from keyboards.inline.smartphones import back_to_samsung_button, back_to_redmi_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="redmi_callback")
@dp.callback_query_handler(text="RedMi_callback")
async def RedMi_callback_func(call: CallbackQuery):
    text = "Smartfonlardan birini tanlang"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/xiami.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="xiaomi_12_callback")
async def xiaomi_12_callback_func(call: CallbackQuery):
    text = '🔻Процессор: Snapdragon 778G+, 8 ядер, 2.4 ГГц\n' \
           '🔻Объем оперативной памяти: 6 Гб\n' \
           '🔻Объем встроенной памяти: 128 ГБ\n' \
           '🔻Экран: 6.55", 2400 * 1080, 120 Гц\n' \
           '🔻Основная камера: 108 МП + 8 МП + 2 МП\n' \
           '🔻Емкость аккумулятора: 4300 мА/ч\n' \
           '🔻Вес: 159 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/xiaomi_12_lite.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="pro_11_callback")
async def pro_11_callback_func(call: CallbackQuery):
    text = '🔻Процессор: Mediatek Helio G96, 8 ядер, 2 ГГц\n' \
           '🔻Экран: 6.43", 2400*1080, AMOLED, 90 Гц\n' \
           '🔻Оперативная память: 8 ГБ\n' \
           '🔻Встроенная память: 128 ГБ\n' \
           '🔻Аккумулятор: 5000 мА/ч\n' \
           '🔻Фронтальная камера: 13 МП\n' \
           '🔻Вес: 179 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/11_pro.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="a1_callback")
async def a1_callback_func(call: CallbackQuery):
    text = '🔻Оперативная память: 2 Гб\n' \
           '🔻Встроенная память: 32 Гб\n' \
           '🔻Процессор: MediaTek Helio A22, 4 ядра, 2 ГГц\n' \
           '🔻Экран: 6.52", 1600 * 720, IPS\n' \
           '🔻Основные камеры: 8 МП + 0.3 МП\n' \
           '🔻Фронтальная камера: 5 МП\n' \
           '🔻Ёмкость аккумулятора: 5000 мА/ч'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/a11.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="a1_callback")
async def a1_callback_func(call: CallbackQuery):
    text = '🔻Процессор: Snapdragon 778G+, 8 ядер, 2.4 ГГц\n' \
           '🔻Объем оперативной памяти: 6 Гб\n' \
           '🔻Объем встроенной памяти: 128 ГБ\n' \
           '🔻Экран: 6.55", 2400 * 1080, 120 Гц\n' \
           '🔻Основная камера: 108 МП + 8 МП + 2 МП\n' \
           '🔻Емкость аккумулятора: 4300 мА/ч\n' \
           '🔻Вес: 159 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/xiaomi_12_lite.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="redmi_10_callback")
async def redmi_10_callback_func(call: CallbackQuery):
    text = '🔻Версия ОС:Android 11\n' \
           '🔻Тип SIM-карты: nano SIM, 2 шт\n' \
           '🔻Диагональ:6.5 дюйма.\n' \
           '🔻Разрешение экрана:2400x1080 пикс\n' \
           '🔻Процессор:2000 МГц\n' \
           '🔻Количество ядер;8\n' \
           '🔻Аккумулятор:5000 мА⋅ч'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/redmi_10.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()


@dp.callback_query_handler(text="redmi_10c_callback")
async def redmi_10c_callback_func(call: CallbackQuery):
    text = '🔻Процессор: Snapdragon 680, 8 ядер, 2.4 ГГц\n' \
           '🔻Оперативная память: 3 ГБ\n' \
           '🔻Встроенная память: 64 ГБ\n' \
           '🔻Основные камеры: 50 МП, 2 МП\n' \
           '🔻Емкость аккумулятора: 5000 мА/ч\n' \
           '🔻Размеры: 169.6 * 76.6 * 8.3 мм\n' \
           '🔻Вес: 190 г'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/redmi/10c.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_redmi_button)
    await call.message.delete()
