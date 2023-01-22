import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)


# Bot obyekti
bot = Bot(token="API_TOKEN")
# Bot uchun dispetcher
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # keyboard obyekti
    buttons = ['Yaxshi','Yomon']
    keyboard.add(*buttons) # yoki .add('Yaxshi','Yomon')
    await message.answer("Kayfiyatingiz qanday?", reply_markup=keyboard)

    
@dp.message_handler(commands="buttons")
async def buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Lokatsiyani yuborish", request_location=True))
    keyboard.add(types.KeyboardButton(text="Telefon raqamni yuborish", request_contact=True))
    await message.answer("Quyidagi maxsus tugmalardan birini tanlang: ", reply_markup=keyboard)

 
@dp.message_handler(Text("Yaxshi"))
async def good(message: types.Message):
    await message.reply("Kayfiyatingiz yaxshi ekanligidan xursandman :)",reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text("Yomon"))
async def bad(message: types.Message):
    await message.reply("Kayfiyatingiz yomonligidan afsusdaman :(\nSizga yaxshi kayfiyat tilab qo'laman!")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
