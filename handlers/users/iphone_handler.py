from keyboards.inline.iphone import iphone_button
from keyboards.inline.smartphones import back_to_samsung_button, back_to_iphone_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text="iphone_callback")
@dp.callback_query_handler(text="Apple_callback")
async def Apple_callback_func(call: CallbackQuery):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/apple.jpg", "rb")
    await call.message.answer_photo(pic, text, reply_markup=iphone_button)
    await call.message.delete()


@dp.callback_query_handler(text="promax_callback")
async def promax_callback_func(call: CallbackQuery):
    text = "🔻Год выпуска: 2022\n" \
           "🔻Объем памяти: 128 ГБ, 256 ГБ, 512 ГБ, 1 ТБ\n" \
           "🔻Цвета: золотой, «черный космос», «темный фиолет»\n" \
           "🔻Номера моделей: A2651 (США, Пуэрто-Рико), A2893 (Гуам, Виргинские острова)\n" \
           "🔻Сведения: устройство iPhone 14 Pro Max оснащено полноэкранным дисплеем Super Retina XDR с диагональю " \
           "6,7 дюйма1. На задней панели — матовое стекло премиум класса, а вокруг рамки — полоса из нержавеющей" \
           " стали. Боковая кнопка расположена с правой стороны устройства. На задней панели корпуса находятся " \
           "три камеры: сверхширокоугольная, основная и с телеобъективом. Также на задней панели корпуса расположен" \
           " сканер LiDAR. На задней панели расположена светодиодная вспышка True Tone. В моделях, продаваемых" \
           " в США, нет лотка SIM-карты. В моделях, продаваемых в других странах и регионах, на левой стороне" \
           " устройства расположен лоток SIM-карты для карт четвертого форм-фактора (4FF) nano-SIM."
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/iphone-14-pro-max.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_iphone_button)
    await call.message.delete()


@dp.callback_query_handler(text="pro_callback")
async def pro_callback_func(call: CallbackQuery):
    text = "🔻Год выпуска:  2022\n" \
           "🔻Объем памяти: 128 ГБ, 256 ГБ, 512 ГБ, 1 ТБ\n" \
           "🔻Цвета: серебристый, золотой, «черный космос», «темный фиолет»\n" \
           "🔻Номера моделей: A2650 (США, Пуэрто-Рико), A2889 (Виргинские острова (США)\n" \
           "🔻Сведения: устройство iPhone 14 Pro Max оснащено полноэкранным дисплеем Super Retina XDR с диагональю " \
           "6,7 дюйма1. На задней панели — матовое стекло премиум класса, а вокруг рамки — полоса из нержавеющей" \
           " стали. Боковая кнопка расположена с правой стороны устройства. На задней панели корпуса находятся " \
           "три камеры: сверхширокоугольная, основная и с телеобъективом. Также на задней панели корпуса расположен" \
           " сканер LiDAR. На задней панели расположена светодиодная вспышка True Tone. В моделях, продаваемых" \
           " в США, нет лотка SIM-карты. В моделях, продаваемых в других странах и регионах, на левой стороне" \
           " устройства расположен лоток SIM-карты для карт четвертого форм-фактора (4FF) nano-SIM."
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/iphone-14-pro.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_iphone_button)
    await call.message.delete()


@dp.callback_query_handler(text="plus_callback")
async def plus_callback_func(call: CallbackQuery):
    text = "🔻Год выпуска:  2022\n" \
           "🔻Объем памяти: 128 ГБ, 256 ГБ, 512 ГБ, 1 ТБ\n" \
           "🔻Цвета: серебристый, золотой, «черный космос», «темный фиолет»\n" \
           "🔻Номера моделей: A2650 (США, Пуэрто-Рико), A2889 (Виргинские острова (США)\n" \
           "🔻Сведения: устройство iPhone 14 Pro Max оснащено полноэкранным дисплеем Super Retina XDR с диагональю " \
           "6,7 дюйма1. На задней панели — матовое стекло премиум класса, а вокруг рамки — полоса из нержавеющей" \
           " стали. Боковая кнопка расположена с правой стороны устройства. На задней панели корпуса находятся " \
           "три камеры: сверхширокоугольная, основная и с телеобъективом. Также на задней панели корпуса расположен" \
           " сканер LiDAR. На задней панели расположена светодиодная вспышка True Tone. В моделях, продаваемых" \
           " в США, нет лотка SIM-карты. В моделях, продаваемых в других странах и регионах, на левой стороне" \
           " устройства расположен лоток SIM-карты для карт четвертого форм-фактора (4FF) nano-SIM."
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/iphone-14-plus.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_iphone_button)
    await call.message.delete()


@dp.callback_query_handler(text="i14_callback")
async def i14_callback(call: CallbackQuery):
    text = "🔻Год выпуска:  2022\n" \
           "🔻Объем памяти: 128 ГБ, 256 ГБ, 512 ГБ, 1 ТБ\n" \
           "🔻Цвета: серебристый, золотой, «черный космос», «темный фиолет»\n" \
           "🔻Номера моделей: A2650 (США, Пуэрто-Рико), A2889 (Виргинские острова (США)\n" \
           "🔻Сведения: устройство iPhone 14 Pro Max оснащено полноэкранным дисплеем Super Retina XDR с диагональю " \
           "6,7 дюйма1. На задней панели — матовое стекло премиум класса, а вокруг рамки — полоса из нержавеющей" \
           " стали. Боковая кнопка расположена с правой стороны устройства. На задней панели корпуса находятся " \
           "три камеры: сверхширокоугольная, основная и с телеобъективом. Также на задней панели корпуса расположен" \
           " сканер LiDAR. На задней панели расположена светодиодная вспышка True Tone. В моделях, продаваемых" \
           " в США, нет лотка SIM-карты. В моделях, продаваемых в других странах и регионах, на левой стороне" \
           " устройства расположен лоток SIM-карты для карт четвертого форм-фактора (4FF) nano-SIM."
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/iphone-14.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_iphone_button)
    await call.message.delete()


@dp.callback_query_handler(text="se_callback")
async def se_callback(call: CallbackQuery):
    text = "🔻Год выпуска:  2022\n" \
           "🔻Объем памяти: 128 ГБ, 256 ГБ, 512 ГБ, 1 ТБ\n" \
           "🔻Цвета: серебристый, золотой, «черный космос», «темный фиолет»\n" \
           "🔻Номера моделей: A2650 (США, Пуэрто-Рико), A2889 (Виргинские острова (США)\n" \
           "🔻Сведения: устройство iPhone 14 Pro Max оснащено полноэкранным дисплеем Super Retina XDR с диагональю " \
           "6,7 дюйма1. На задней панели — матовое стекло премиум класса, а вокруг рамки — полоса из нержавеющей" \
           " стали. Боковая кнопка расположена с правой стороны устройства. На задней панели корпуса находятся " \
           "три камеры: сверхширокоугольная, основная и с телеобъективом. Также на задней панели корпуса расположен" \
           " сканер LiDAR. На задней панели расположена светодиодная вспышка True Tone. В моделях, продаваемых" \
           " в США, нет лотка SIM-карты. В моделях, продаваемых в других странах и регионах, на левой стороне" \
           " устройства расположен лоток SIM-карты для карт четвертого форм-фактора (4FF) nano-SIM."
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/iphone/iphone-se-3rd-gen.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=back_to_iphone_button)
    await call.message.delete()



