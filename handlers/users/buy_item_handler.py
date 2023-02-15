from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.menu import menu_button

from data.config import ADMINS
from keyboards.default.contact_info import res_button
from loader import dp
from states.personal_info import PersonalData


@dp.callback_query_handler(text="buy_item")
async def registration_func(call: CallbackQuery):
    text = "Haridni yakunlash uchun locatsiyani kiriting\n" \
           "Mazilingizni yozib jonating"
    await call.message.answer(text)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.location)
async def answer_fullname(msg: Message, state: FSMContext):
    location = msg.text
    await state.update_data(
        {"Location": location}
    )
    text = "Telefon raqamini jonating"
    await msg.answer(text, reply_markup=ReplyKeyboardRemove())
    await PersonalData.next()


@dp.message_handler(state=PersonalData.number)
async def phone_function(msg: Message, state: FSMContext):
    number = msg.text
    await state.update_data(
        {"number": number}
    )
    data = await state.get_data()
    location = data.get("Location")
    phone_number = data.get("number")

    text = f"Quidagi ma'lumotlar qabul qilindi: \n" \
           f"\n" \
           f"Manzil: {location} \n" \
           f"\n" \
           f"Raqamingiz: {phone_number} \n" \
           f"\n" \
           f"Agar berilgan malumotlar to'gri bo'lsa Ha ni, to'g'irlamoqchi bo'lsangiz Yo'q ni bosin"

    await msg.answer(text, reply_markup=res_button)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.responce)
async def phone_function(msg: Message, state: FSMContext):
    responce = msg.text
    if responce == "Ha":
        data = await state.get_data()
        location = data.get("Location")
        phone_number = data.get("number")

        text = f"Raqam: {phone_number} \n" \
               f"\n" \
               f"Manzil: {location} \n" \
               f"\n"
        for admin in ADMINS:
            await dp.bot.send_message(admin, text)
        await msg.answer(f"Salom, {msg.from_user.full_name}!", reply_markup=menu_button)
        await state.finish()

    elif responce == "Yo'q":
        await msg.answer("Manzilingizni kiriting 👇", reply_markup=ReplyKeyboardRemove())
        await PersonalData.location.set()
