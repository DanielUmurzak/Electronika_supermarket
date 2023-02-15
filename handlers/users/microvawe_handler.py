from keyboards.inline.microvawe import microvawe_button, microvawe_washing
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="microwave_callback")
async def beko_moc20100s_callback_func(call: CallbackQuery):
    text = "Bizning microvalnovkalar:"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/microvawe/micro.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=microvawe_button)
    await call.message.delete()


@dp.callback_query_handler(text="beko_moc20100s_callback")
async def beko_moc20100s_callback_func(call: CallbackQuery):
    text = "🔻Высота 26.2 см\n" \
           "🔻Ширина 45.2 см\n" \
           "🔻Глубина 32.5 см\n" \
           "🔻Вес нетто 10.7 кг\n" \
           "🔻Объем 20 л\n" \
           "🔻Мощность микроволн 700\n" \
           "🔻Диаметр блюда 245 мм\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/microvawe/BEKO MOC20100S.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=microvawe_washing)
    await call.message.delete()


@dp.callback_query_handler(text="samsung_me_81_callback")
async def samsung_me_81_callback_func(call: CallbackQuery):
    text = "🔻Исполнение - отдельностоящая\n" \
           "🔻Тип - микроволны (соло)\n" \
           "🔻Цвет - белый\n" \
           "🔻Объем - 23 л\n" \
           "🔻Мощность - 1 150 Вт\n" \
           "🔻Количество уровней мощности - 7\n" \
           "🔻Выходная мощность микроволн - 800 Вт\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/microvawe/Samsung ME 81 ARW White.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=microvawe_washing)
    await call.message.delete()


@dp.callback_query_handler(text="goodwell_gmf_callback")
async def goodwell_gmf_callback_func(call: CallbackQuery):
    text = "🔻Исполнение - отдельностоящая\n" \
           "🔻Тип - микроволны (соло)\n" \
           "🔻Цвет - белый\n" \
           "🔻Объем - 23 л\n" \
           "🔻Мощность - 1 150 Вт\n" \
           "🔻Количество уровней мощности - 7\n" \
           "🔻Выходная мощность микроволн - 800 Вт\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/microvawe/Goodwell GMF 2301 BL.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=microvawe_washing)
    await call.message.delete()


@dp.callback_query_handler(text="hofman_hmw_callback")
async def hofman_hmw_callback_func(call: CallbackQuery):
    text = "🔻Внутренний объем:	20 л\n" \
           "🔻Таймер:	Есть\n" \
           "🔻Мощность микроволн, Вт:	700\n" \
           "🔻Количество уровней мощности:	5\n" \
           "🔻Программы:	Режим разморозки\n" \
           "🔻Вес:	15.5 кг\n" \
           "🔻Размеры (ШxВxГ):	430 x 260 x 340 мм\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/microvawe/Hofmann HMW-720SS 20 л.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=microvawe_washing)
    await call.message.delete()
