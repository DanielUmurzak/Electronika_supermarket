from keyboards.inline.samsung import samsung_button, back_laptops
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="samsung_callback")
async def samsung_callback_func(call: CallbackQuery):
    text = "Noutbooklarimiz"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung_lap/samsung1.jpeg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=samsung_button)
    await call.message.delete()


@dp.callback_query_handler(text="pro_15_360_callback")
async def pro_16_m2_callback_func(call: CallbackQuery):
    text = "🔻Экран: 15.6 FHD TouchScreen AMOLED (1920 x 1080)\n" \
           "🔻Процессор: Intel® Core™ i7-1165G7 (1.2GHz – 4.7GHz) (4-Ядра; 8-Потоков)\n" \
           "🔻Видеокарта: Intel Iris Xe Graphics\n" \
           "🔻ОЗУ: 16GB DDR4\n" \
           "🔻Накопитель: 1TB PCIe® NVMe™ M.2 SSD\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung_lap/Pro 15 360 (i7-1165G7).jpg",
               "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pro_15_i5_callback")
async def pro_15_i5_callback_func(call: CallbackQuery):
    text = "🔻Процессор: Intel Core i5-1135G7 (2.4 GHz – 4.2 GHz) (4-Ядрa; 8-Потоков;)\n" \
           "🔻Видеокарта: Intel Iris Xe Graphics\n" \
           "🔻ОЗУ: 8GB DDR4\n" \
           "🔻Накопитель: 512GB PCIe® NVMe™ M.2 SSD\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung_lap/i5(1135g7).jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="flex_callback")
async def flex_callback_callback_func(call: CallbackQuery):
    text = "🔻Экран: 13.3 FullHD QLED TouchScreen\n" \
           "🔻Процессор: Intel® Core™ i7-1165G7 (1.2GHz – 4.7GHz) (4-Ядра; 8-Потоков)\n" \
           "🔻ОЗУ: 16GB DDR4\n" \
           "🔻Видеокарта: Intel Iris Xe Graphics\n" \
           "🔻Накопитель: 512GB PCIe® NVMe™ M.2 SSD"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung_lap/flex.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pro_360_13_callback")
async def pro_360_13_callback_func(call: CallbackQuery):
    text = "🔻Экран: 13.3'' FullHD AMOLED (1920 x 1080) TouchScreen\n" \
           "🔻Процессор: Intel® Core™ i7-1165G7 (1.2GHz – 4.7GHz) (4-Ядра; 8-Потоков)\n" \
           "🔻Видеокарта: Intel Iris Xe Graphics\n" \
           "🔻ОЗУ: 16GB DDR4\n" \
           "🔻Накопитель: 512GB PCIe® NVMe™ M.2 SSD (1TB SSD=+80 у.е)"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/samsung_lap/pro_13_360.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()
