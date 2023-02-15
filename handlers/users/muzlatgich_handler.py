from keyboards.inline.muzlatgich import xolodilnik_button, backto_fridge
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="muzlatgich_callback")
async def muzlatgich_callback_func(call: CallbackQuery):
    text = "Bizning Muzlatgichlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/xol.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=xolodilnik_button)
    await call.message.delete()


@dp.callback_query_handler(text="roison_callback")
async def roison_callback_func(call: CallbackQuery):
    text = "🔻Климатическая категория - N,ST\n" \
           "🔻Защитная классификация электро-ударного сопротивления - I\n" \
           "🔻Номинальное напряжение - 220-240V\n" \
           "🔻Номинальная частота - 50Hz\n" \
           "🔻Номинальный ток - 0,9А\n" \
           "🔻Общий объем - 205L\n" \
           "🔻Система разморозки - Defrost\n" \
           "🔻Полки - Стекло / 3 шт\n" \
           "🔻Тип управления - механическое"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/Roison RHWG DF2-27 W.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_fridge)
    await call.message.delete()


@dp.callback_query_handler(text="atlant_callback")
async def atlant_callback_func(call: CallbackQuery):
    text = "🔻Климатическая категория - N,ST\n" \
           "🔻Категория холодильного прибора7\n" \
           "🔻Система охлаждения  FULL NO FROST\n" \
           "🔻Класс энергоэффективности  А\n" \
           "🔻Уровень шума  43 дБА\n" \
           "🔻лиматический класс  SN, N, ST\n" \
           "🔻Система разморозки - Defrost\n" \
           "🔻Номинальная потребляемая мощность 100 Вт\n" \
           "🔻Номинальное напряжение и частота  220-230 В ~ 50 Гц"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/Atlant ХМ-4421-000-N.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_fridge)
    await call.message.delete()


@dp.callback_query_handler(text="tcl_callback")
async def tcl_callback_func(call: CallbackQuery):
    text = "🔻Электронное управление\n" \
           "🔻Дозатор воды\n" \
           "🔻Ящики нового типа\n" \
           "🔻Точная температура. Контроль\n" \
           "🔻Регулируемая полка\n" \
           "🔻Полное отсутствие мороза\n" \
           "🔻LED подсветка\n" \
           "🔻Двойной Эко-инвертор\n" \
           "🔻Энергетический класс EU - A+"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/TCL Invertor Total No Frost.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_fridge)
    await call.message.delete()


@dp.callback_query_handler(text="beko_callback")
async def tcl_callback_func(call: CallbackQuery):
    text = "🔻Высота-145.8 см\n" \
           "🔻Ширина-54 см\n" \
           "🔻Глубина-60 см\n" \
           "🔻Общий объем-240 л\n" \
           "🔻Класс энергопотребления - A\n" \
           "🔻Морозильная камера - С верхней морозильной камерой\n" \
           "🔻LED подсветка\n" \
           "🔻Уровень шума (дБ) - 40\n" \
           "🔻Энергетический класс EU - A+"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/beko.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_fridge)
    await call.message.delete()
