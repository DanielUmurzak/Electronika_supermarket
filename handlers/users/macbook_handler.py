from keyboards.inline.macbook import macbook_button, back_laptops
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="macbook_callback")
async def hp_callback_func(call: CallbackQuery):
    text = "Noutbooklarimiz"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/macbook/apple.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=macbook_button)
    await call.message.delete()


@dp.callback_query_handler(text="pro_16_m2_callback")
async def pro_16_m2_callback_func(call: CallbackQuery):
    text = "🔻Дисплей:16.2 , 3456x2234\n" \
           "🔻Процессор:Apple M2 Pro\n" \
           "🔻Оперативка:16 ГБ\n" \
           "🔻Накопитель:SSD, 512 ГБ\n" \
           "🔻ОС:MacOS\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/macbook/MacBook Pro 16-inch.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pro_14_m2_callback")
async def pro_14_m2_callback_func(call: CallbackQuery):
    text = "🔻Дисплей:14.2 , 3024x1964\n" \
           "🔻Процессор:Apple M2 Pro\n" \
           "🔻Оперативка:16 ГБ\n" \
           "🔻Накопитель:SSD, 512 ГБ\n" \
           "🔻ОС:MacOS\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/macbook/pro_14_m2.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pro_16_m1_callback")
async def pro_16_m1_callback_func(call: CallbackQuery):
    text = "🔻Процессор: M1 Pro \n" \
           "🔻ОЗУ: 16 ГБ\n" \
           "🔻Встроенный память: 512 ГБ\n" \
           "🔻исплей: Liquid Retina XDR 16,2 дюймов\n" \
           "🔻Клавиатура: Magic Keyboard с Touch ID\n" \
           "🔻Вес: 1.6 Кг\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/macbook/pro_16_m1.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pro_14_m1_callback")
async def pro_14_m1_callback_func(call: CallbackQuery):
    text = "🔻Процессор: M1 Pro \n" \
           "🔻ОЗУ: 16 ГБ\n" \
           "🔻Встроенный память: 4TB\n" \
           "🔻16‑ядерная сисема: Neural Engine\n" \
           "🔻Дисплей: Liquid Retina XDR 14,2 дюймов\n" \
           "🔻Адаптер питания: USB‑C мощностью 140 Вт\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/macbook/pro_14_m1.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()