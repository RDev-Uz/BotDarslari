from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    ism = State()
    familiya = State()
    yosh = State()
