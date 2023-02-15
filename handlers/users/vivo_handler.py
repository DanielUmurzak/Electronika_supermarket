from keyboards.inline.vivo import vivo_button, back_to_vivo_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="vivo_callback")
@dp.callback_query_handler(text="Vivo_callback")
async def Vivo_callback_func(call: CallbackQuery):
    text = "Smartfonlardan birini tanlang"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/Vivo-Logo.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=vivo_button)
    await call.message.delete()


@dp.callback_query_handler(text="y02_callback")
async def y02_callback_func(call: CallbackQuery):
    text = '🔻Встроенная память 32 ГБ\n' \
           '🔻Оперативная память 2 ГБ\n' \
           '🔻Беспроводные интерфейсы Wi-Fi, Bluetooth\n' \
           '🔻Количество SIM-карт Dual SIM (nano SIM)\n' \
           '🔻Процессор Mediatek Helio P22 (MT6762R)\n' \
           '🔻Цвет голубой,черный'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/Vivo Y02.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_vivo_button)
    await call.message.delete()


@dp.callback_query_handler(text="v25_callback")
async def v25_callback_func(call: CallbackQuery):
    text = '🔻Процессор MediaTek Helio G99\n' \
           '🔻Оперативная память 8 ГБ\n' \
           '🔻Встроенная память 128 ГБ/ 256 ГБ\n' \
           '🔻Аккумулятор 4500 мА·ч (типовое значение) \n' \
           '🔻Мощность зарядки 44 Вт быстрая зарядка (11 В/4 А)\n' \
           '🔻Операционная система Funtouch OS 12'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/vivo V25e.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_vivo_button)
    await call.message.delete()


@dp.callback_query_handler(text="y22_callback")
async def y22_callback_func(call: CallbackQuery):
    text = '🔻Встроенная память\n' \
           '🔻64 ГБ Оперативная память\n' \
           '🔻4 ГБ Беспроводные интерфейсы\n' \
           '🔻Wi-Fi, Bluetooth, NFC Количество SIM-карт\n' \
           '🔻Dual SIM (nano SIM)Процессор\n' \
           '🔻MediaTek Helio G85 Цвет'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/vivo Y22.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_vivo_button)
    await call.message.delete()


@dp.callback_query_handler(text="y15s_callback")
async def y15s_callback_func(call: CallbackQuery):
    text = '🔻Процессор Helio P35\n' \
           '🔻Оперативная память 3 ГБ\n' \
           '🔻Встроенная память 32 ГБ\n' \
           '🔻Аккумулятор 5000 мА·ч\n' \
           '🔻Цвет Таинственный синий, Зелёная \n' \
           '🔻Операционная система Funtouch OS 11.1'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/Vivo Y15S.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_vivo_button)
    await call.message.delete()


@dp.callback_query_handler(text="y53_callback")
async def y53_callback_func(call: CallbackQuery):
    text = '🔻Встроенная память 128\n' \
           '🔻Оперативная память 8 ГБ\n' \
           '🔻Беспроводные интерфейсы Wi-Fi, Bluetooth, NFC\n' \
           '🔻Количество SIM-карт Dual SIM (nano SIM)\n' \
           '🔻Процессор MediaTek Helio G80\n' \
           '🔻Цвет синий, голубой'
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/vivo/vivo Y53s.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_vivo_button)
    await call.message.delete()
