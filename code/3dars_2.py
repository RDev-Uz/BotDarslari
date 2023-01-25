import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from random import randint

# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)


# Bot obyekti
bot = Bot(token="API_TOKEN")
# Bot uchun dispetcher
dp = Dispatcher(bot)


@dp.message_handler(commands='random')
async def random_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Tugmani bosing",callback_data='random_value'))
    await message.answer("1dan 10gacha bo'lgan tasodifiy sonlarni jo'natishim uchun quyidagi tugmani bosing: ", reply_markup=keyboard)


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.edit_text(str(randint(1,10)))


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
