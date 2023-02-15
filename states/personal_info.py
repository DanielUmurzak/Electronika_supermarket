from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    location = State()
    number = State()
