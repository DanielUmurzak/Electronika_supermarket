from keyboards.inline.washing_machine import washing_button, backto_washing
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="washing_machin_callback")
async def washing_machin_callback_func(call: CallbackQuery):
    text = "Bizning kir yuvishni moshinalari:"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/washing_machine/washing_m.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=washing_button)
    await call.message.delete()


@dp.callback_query_handler(text="tcl_combo_callback")
async def roison_callback_func(call: CallbackQuery):
    text = "🔻Тип загрузки - фронтальная. Тип управления - механические кнопки; электромеханическое\n" \
           "🔻Дисплей - есть. Тип дисплея - цифровой (символьный)\n" \
           "🔻Прямой привод - да. Максимальная загрузка белья - 10 кг\n" \
           "🔻Сушка - есть (до 6 кг). Стирка паром - есть. Таймер окончания стирки - есть.\n" \
           "🔻Максимальное время отсрочки старта - 24 ч. Расход воды за стирку - 55 л. Количество программ стирки - 15\n" \
           "🔻Максимальная скорость отжима - 1200 об/мин. Уровень шума при отжиме - 72 дБ\n" \
           "🔻Класс стирки - A. Класс отжима - B. Класс энергопотребления - A++\n" \
           "🔻Для получения дополнительной информации перейдите в раздел «Состав», «Размеры» или «Подробности»\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/xolodilnik/TCL Invertor Total No Frost.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_washing)
    await call.message.delete()


@dp.callback_query_handler(text="bosch_callback")
async def bosch_callback_func(call: CallbackQuery):
    text = "🔻Загрузка: 9 кг\n" \
           "🔻Класс энергоэффективности: A+++\n" \
           "🔻Отжим: 1200 Об/мин\n" \
           "🔻Количество программ: 15\n" \
           "🔻Тип управления: электронное\n" \
           "🔻Вес: 72 кг\n" \
           "🔻Габариты (В х Ш х Г): 848 x 598 x 590 мм\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/washing_machine/Bosch WGA242X0ME.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_washing)
    await call.message.delete()


@dp.callback_query_handler(text="beko_wspe_callback")
async def beko_wspe_callback_func(call: CallbackQuery):
    text = "🔻Вес 62 кг Габариты 84×60×45 см Марка Beko\n" \
           "🔻Тип двигателя инвертор\n" \
           "🔻Максимальная загрузка для стирки, кг 7,5\n" \
           "🔻Расход воды на стирку, л 55\n" \
           "🔻Потребление электроэнергии, кВт/час 1,125\n" \
           "🔻Максимальная скорость вращения, м/мин 1200\n" \
           "🔻Потребляемая мощность 2200 Вт\n" \
           "🔻Частота, Гц50"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/washing_machine/BEKO WSPE6H616S.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_washing)
    await call.message.delete()


@dp.callback_query_handler(text="haier_hwd_callback")
async def haier_hwd_callback_func(call: CallbackQuery):
    text = "🔻Тип мотора Инверторный\n" \
           "🔻Цвет Серебристый\n" \
           "🔻Количество программ 14\n" \
           "🔻Дисплей ЕстьКласс энергопотребления\n" \
           "🔻B Габариты (ВxШxГ), см85х59,5х45,3\n" \
           "🔻Тип загрузкиФронтальнаяПрограммыСушка, Синтетика, Смешанные ткани, Шерсть, Ежедневная стирка," \
           " Экспресс-стирка 15 мин, Отжим, Гигиена, Детская одежда, Хлопок+, Очистка барабана, UV обработка, " \
           "Пуховое одеяло, Стирка&Сушка 59'Максимальная загрузка белья (стирка), кг8Максимальная загрузка белья" \
           " (сушка), кг5Скорость отжима, об/мин1400Класс эффективности стиркиAКласс эффективности отжимаBВес," \
           " кг61УправлениеЭлектронноеСтранаКитай\n"
    pic = open(
        "D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/washing_machine/Haier HWD80-BP14979S.jpg",
        "rb")
    await call.message.answer_photo(pic, text, reply_markup=backto_washing)
    await call.message.delete()
