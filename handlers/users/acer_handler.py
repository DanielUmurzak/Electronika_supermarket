from keyboards.inline.acer import acer_button, back_laptops
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="acer_callback")
async def acer_callback_func(call: CallbackQuery):
    text = "Noutbooklarimiz"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/acer/acer.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=acer_button)
    await call.message.delete()


@dp.callback_query_handler(text="aspire_callback")
async def aspire_callback_func(call: CallbackQuery):
    text = "🔻Диагональ: 15,6″ - 39,62 см \n" \
           "🔻Процессор: Intel® Core™ i3\n" \
           "🔻Операционная система: Без операционной системы \n" \
           "🔻Объем оперативной памяти: 4 GB \n" \
           "🔻Тип жесткого диска: HDD\n" \
           "🔻Объем накопителя: 1 TB \n" \
           "🔻Серия видеокарты: Intel UHD Graphics\n" \
           "🔻Чипсет видеоадаптера: Graphics\n "
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/acer/Acer_A315-35_C83X_N4500_4GB_1000GB_Pure_Silver.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="s5_callback")
async def s5_callback_func(call: CallbackQuery):
    text = "🔻ПроцессорIntel Core i5-6200U 2 x 2.3 - 2.8 GHz, Skylake\n" \
           "🔻Графический адаптерIntel HD Graphics 520\n" \
           "🔻ОЗУ8 Гбайт\n" \
           "🔻Дисплей13.30 дюйм. 16:9, 1920 x 1080 пикс \n" \
           "🔻Хранение данных 256 GB SSD\n" \
           "🔻Интерфейсы 3 USB 3.0 / 3.1 Gen 1, 1 HDMI\n" \
           "🔻Операционная системаMicrosoft Windows 10 Home 64 Bit\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/acer/S5-371T.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="swift_callback")
async def swift_callback_func(call: CallbackQuery):
    text = "🔻ПроцессорIntel Core i5-6200U 2 x 2.3 - 2.8 GHz, Skylake\n" \
           "🔻Графический адаптерIntel HD Graphics 520\n" \
           "🔻ОЗУ8 Гбайт\n" \
           "🔻Дисплей13.30 дюйм. 16:9, 1920 x 1080 пикс \n" \
           "🔻Хранение данных 256 GB SSD\n" \
           "🔻Интерфейсы 3 USB 3.0 / 3.1 Gen 1, 1 HDMI\n" \
           "🔻Операционная системаMicrosoft Windows 10 Home 64 Bit\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/acer/SF314-511.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="ex215_callback")
async def ex215_callback_func(call: CallbackQuery):
    text = "🔻Процессор: Intel Core i3 1005G1\n" \
           "🔻Оперативная память: 4 ГБ\n" \
           "🔻Жесткий диск: 1000 ГБ\n" \
           "🔻Дисплей13.30 дюйм. 16:9, 1920 x 1080 пикс \n" \
           "🔻Хранение данных 256 GB SSD\n" \
           "🔻Интерфейсы 3 USB 3.0 / 3.1 Gen 1, 1 HDMI\n" \
           "🔻Операционная системаMicrosoft Windows 10 Home 64 Bit\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/acer/EX215-52.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()