import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import Form


logging.basicConfig(level=logging.INFO)


bot = Bot(token="API_TOKEN",parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot,storage=MemoryStorage()) # FSM uchun MemoryStorage'ni ulaymiz


def cancel_btn():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Bekor qilish")
    return keyboard


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await Form.ism.set() # Ismni qabul qilishni sozlaymiz
    await message.answer(
        "Assalomu Alaykum!\n\nIsmingizni kiriting: ",
        reply_markup=cancel_btn(),
    )


@dp.message_handler(text="Bekor qilish",state='*')
async def cancel_state(message: types.Message,state: FSMContext):
    await message.answer(
        "Ro'yxatdan o'tish bekor qilindi!\n\n"
        "Qayta ro'yxatdan o'tmoqchi bo'lsangiz /start buyrug'ini jo'nating.",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await state.finish()


@dp.message_handler(state=Form.ism)
async def get_ism(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text) # State'dagi ism qiymatini yangilaymiz
    await Form.next() # Kengi State'ga o'tkazamiz
    await message.answer(
        "Endi familiyangizni kiriting: ",
        reply_markup=cancel_btn(),
    )


@dp.message_handler(state=Form.familiya)
async def get_familiya(message: types.Message,state: FSMContext):
    await state.update_data(familiya=message.text)
    await Form.next() # Kengi State'ga,yani yoshga o'tkazamiz
    await message.answer(
        "Yaxshi, endi yoshingizni kiriting: ",
        reply_markup=cancel_btn(),
    )


@dp.message_handler(state=Form.yosh)
async def finish_state(message: types.Message,state: FSMContext):
    if message.text.isdigit() is False:
        await message.answer(
            "Iltimos, yoshingizni kiriting!",
            reply_markup=cancel_btn(),
        )
        return
    data = await state.get_data() # State'dagi qiymatlarni olamiz
    await message.answer(
        "Ma'lumotlar muvaffaqiyatli qabul qilindi!\n\n"
        f"Ismingiz: <b>{data['ism']}</b>\n"
        f"Familiyangiz: <b>{data['familiya']}</b>\n"
        f"Yoshingiz: <b>{message.text}</b>",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await state.finish() # Stateni tugatamiz


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
