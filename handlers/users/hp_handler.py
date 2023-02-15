from keyboards.inline.hp import back_laptops
from keyboards.inline.hp import hp_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="hp_callback")
async def hp_callback_func(call: CallbackQuery):
    text = "Noutbooklarimiz"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/hp/hp.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=hp_button)
    await call.message.delete()


@dp.callback_query_handler(text="victus_callback")
async def victus_callback_func(call: CallbackQuery):
    text = "🔻Экран: 16,1\n" \
           "🔻Процессор: R7-5800H\n" \
           "🔻Оперативная память: 16 ГБ\n" \
           "🔻Жесткий диск: 512 ГБ\n" \
           "🔻Видеокарта: 	VGA4 RTX3050TI\n" \
           "🔻Размеры: 370 x 260 x 23.5 мм\n" \
           "🔻Вес: 	2.4 Кг\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/hp/pavelion.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="pavilion_callback")
async def pavilion_callback_func(call: CallbackQuery):
    text = "🔻Экран: 15.6 \n" \
           "🔻Процессор: R5-5500U\n" \
           "🔻Оперативная память: 8 ГБ\n" \
           "🔻Жесткий диск: 256 ГБ\n" \
           "🔻Видеокарта: -\n" \
           "🔻Размеры: 360.2x234x17.9 мм\n" \
           "🔻Вес: 	1.75 кг\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/hp/pavel.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="s15_callback")
async def s15_callback_func(call: CallbackQuery):
    text = "🔻Экран: 15 \n" \
           "🔻Процессор: N4500\n" \
           "🔻Оперативная память: 4 ГБ\n" \
           "🔻Жесткий диск: 256 ГБ\n" \
           "🔻Видеокарта: -\n" \
           "🔻Размеры: 358.5 x 242 x 17.9 мм\n" \
           "🔻Вес: 	1.75 кг\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/hp/15S-FQ3043UR.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()


@dp.callback_query_handler(text="x360_callback")
async def x360_callback_func(call: CallbackQuery):
    text = "🔻Экран: 15 \n" \
           "🔻Процессор: Intel Core i3 1125G4\n" \
           "🔻Оперативная память: 8 ГБ\n" \
           "🔻Жесткий диск: 256 ГБ\n" \
           "🔻Видеокарта: -\n" \
           "🔻Размеры: 322х209х19,9 мм\n" \
           "🔻Вес: 	1.75 кг\n"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/hp/15S-FQ3043UR.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_laptops)
    await call.message.delete()