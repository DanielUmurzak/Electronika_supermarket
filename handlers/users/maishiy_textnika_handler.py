from keyboards.inline.maishi_textnika import maishiy_button
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.message_handler(text="🔌 Maishiy texnika")
async def phone_button_func(msg: Message):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/maishiy_tex.png", "rb")
    await msg.answer_photo(pic, text, reply_markup=maishiy_button)


@dp.callback_query_handler(text="back_to_maishiy")
async def back_to_maishiy_func(call: CallbackQuery):
    text = "Bizning smartfonlar:"
    pic = open("D:/programming/Telegram_bots/Electronika_supermarket/photos/maishi_texnika/maishiy_tex.png", "rb")
    await call.message.answer_photo(pic, text, reply_markup=maishiy_button)
    await call.message.delete()
