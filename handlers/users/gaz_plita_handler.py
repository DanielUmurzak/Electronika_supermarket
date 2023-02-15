from keyboards.inline.gaz_plita import gaz_plita_button, back_to_gaz_plita
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="gaz_plita_callback")
async def gaz_plita_callback_func(call: CallbackQuery):
    text = "Bizning gaz plitalar:"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/gaz plita/gaz.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=gaz_plita_button)
    await call.message.delete()


@dp.callback_query_handler(text="gefest_pg_callback")
async def gefest_pg_callback_func(call: CallbackQuery):
    text = "🔻Количество зон приготовления:  4\n" \
           "🔻Крышка:  металлическая крышка\n" \
           "🔻Масса нетто, кг:  42.7\n" \
           "🔻Масса брутто, кг:  48.2\n" \
           "🔻Диапазон номинальных напряжений, В:  220-230\n" \
           "🔻Присоединительная резьба газопровода:  G 1/2\n" \
           "🔻Габаритные размеры ШхГхВ, см:  60x60x85\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/gaz plita/Gefest ПГ 6100-02 0309.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_gaz_plita)
    await call.message.delete()


@dp.callback_query_handler(text="artel_apetito_callback")
async def artel_apetito_callback_func(call: CallbackQuery):
    text = "🔻Объем духовки, л	65,0\n" \
           "🔻Количество режимов работы	2,0\n" \
           "🔻Источник питания	220 B / 50 Гц\n" \
           "🔻Мощность верхнего ТЭНа духовки, Вт\n" \
           "🔻Количество газовых горелок рабочего стола, шт	4,0\n" \
           "🔻Газ-контроль рабочего стола\n" \
           "🔻Никелированная решетка духовки, шт	1,0\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/gaz plita/Artel Apetito.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_gaz_plita)
    await call.message.delete()


@dp.callback_query_handler(text="biryusa_u60gg12ss_callback")
async def biryusa_u60gg12ss_callback_func(call: CallbackQuery):
    text = "🔻газ горелок - 4\n" \
           "🔻электро поджиг - есть\n" \
           "🔻вертель (гриль) - есть\n" \
           "🔻поднос - 2\n" \
           "🔻решетка в духовке - 1\n" \
           "🔻духовка верх горелка - электро\n" \
           "🔻духовка низ горелка - газ\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/gaz plita/Бирюса U60GG12SS.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_gaz_plita)
    await call.message.delete()


@dp.callback_query_handler(text="biryusa_u90gg90ss_callback")
async def biryusa_u90gg90ss_callback_func(call: CallbackQuery):
    text = "🔻Кол-во конфорок: 5(газ)\n" \
           "🔻Механический таймер\n" \
           "🔻Чугунная решетка\n" \
           "🔻Газ контроль\n" \
           "🔻Габариты (см): 85х90х60\n" \
           "🔻 Верхняя горелка: электр\n" \
           "🔻Термостат\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/gaz plita/Бирюса U90GG90SS.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_gaz_plita)
    await call.message.delete()