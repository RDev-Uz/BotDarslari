import logging
from aiogram import Bot, Dispatcher, executor, types


# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)

# Bot obyekti
bot = Bot(token="5877758914:AAHji8ugLFHJ7Co7rAj1P8BRq_PyPmLSgYQ")
# Bot uchun dispetcher
dp = Dispatcher(bot)

# Botga jo'natilgan /start buyrug'ini qabul qilib olish uchun handler
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    # foydalanuvchiga javoban salom beradi
    await message.answer("Assalomu alaykum!")

# Foydalanuvchidan kelgan matnni(textni) qabul qilib olish uchun handler
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    # Foydalanuvchi jo'natgan matnga javoban jo'natgan matnini o'ziga yuboradi
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
