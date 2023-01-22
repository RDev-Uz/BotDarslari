import logging
from aiogram import Bot, Dispatcher, executor, types


# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)

# Bot obyekti
bot = Bot(token="API_TOKEN")
# Bot uchun dispetcher
dp = Dispatcher(bot)


@dp.message_handler(commands=['format'])
async def formating(message: types.Message):
    # HTML
    await message.answer(
        text="<b>Black</b>, <i>italic</i>, <u>underline</u>, <s>strikethrough</s>, <a href='https://example.com'>link</a>, <tg-spoiler>spoiler</tg-spoiler>\n\nHTML",
        parse_mode='HTML',
    )
    # MarkdownV2
    await message.answer(
        text="*Black*, _italic_, __underline__, ~strikethrough~, [link](https://example.com), ||spoiler||\n\nMarkdownV2",
        parse_mode='MarkdownV2')
    
   
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
