# **1-dars (kirish)**

Assalomu Alaykum. Ushbu kursimizda siz bilan python dasturlash tilida, aiogram kutubxonasida Telegram Bot tuzishni o'rganamiz. 

Aiogram python dasturlash tilida Telegram Bot yozish uchun eng mashhur kutubxonalardan biri hisoblanadi. Ushbu kutubxona ham boshqa Telegram Bot tuzish uchun mo'ljallangan kutubxonalar kabi [Telegram Bot API](https://core.telegram.org/bots/api)'dan kelayotgan yangilanishlarni olish ([GetUpdates](https://core.telegram.org/bots/api#getupdates)) va foydalanuvchilarga javob qaytarish uchun ishlab chiqilgan bo'lib,katta jamoa(community) tomonidan rivojlantirib kelinmoqda.

### Kursimiz uchun sizga kerak bo'ladi:
- Kamida Python'ning 3.7 versiyasi o'rnatilgan bo'lishi;
- Python dasturlash tilini kamida boshlang'ich darajada bilish;
- pip va venv (virtual environment) bilan ishlashni bilish.

### Foydali manbalar:
- [docs.aiogram.dev](https://docs.aiogram.dev/en/latest/) (Aiogram dakumentatsiyasi)
- [stackoverflow.com](https://stackoverflow.com/) (Xatolarga yechim topish uchun)
- [@aiogram_uz](https://t.me/aiogram_uz) (Aiogram bo'yicha savollar uchun telegram guruh)


### Kursimizning mundarijasi:
- BotFather orqali bot ochish
- Xabarlar bilan ishlash;
- Tugmalar bilan ishlash;
- Ketma-ketlik bo'yicha foydalanuvchidan ma'lumotlarni qabul qilish;
- Inline rejim bilan ishlash.

## **BotFather orqali bot ochish**
1. Dastlab [@BotFather](https://t.me/BotFather)'ni telegramdagi qidiruv qismidan qidirib olamiz:

![1-dars_2](/images/1_dars_2.png)

> Rasmdagi kabi rasmiy belgisi bor bot haqiqiy [@BotFather](https://t.me/BotFather) hisoblanadi.
2. Botga kirganingizdan so'ng "Запустить" (Boshlash,Start) tugmasini bosing.
> Bunga javoban bot sizga botdagi mavjud buyruqlarni yuboradi.
3. "`/newbot`" buyrug'ini yuboring.
4. O'chmoqchi bo'lgan botingizni nomini kiriting;
5. O'chmoqchi bo'lgan botingizning username'ni kiriting;
> Bot username'mining oxiri bot so'zi bilan tugashi shart!

Bot muvvaffaqiyatli ochilgan bo'lsa BotFather sizga shunday xabar jo'natadi:
![1-dars_3](/images/1_dars_3.jpg)


## **Kirish qismi**
Keling avval bizga kerakli kutubxonani, yani Aiogram'ni o'rnatib olamiz:
```console
pip install aiogram
```
> Kod yozishga kirishishdan avval alohida vertual muhut yaratib olish tavsiya etiladi! 

Bot yozish uchun yangi papka yaratib olib,o'sha papkaning ichida `bot.py` nomli fayl yaratib olamiz.
Endi kod yozish qismiga o'tsak bo'ladi,quyidagi kodni `bot.py` faylimizga yozamiz:
```python 
import logging
from aiogram import Bot, Dispatcher, executor, types


# Muhim xabarlarni o'tkazib yubormaslik uchun loglarni sozlab, yoqib qo'yamiz
logging.basicConfig(level=logging.INFO)

# Bot obyekti
bot = Bot(token="API_TOKEN")
# Bot uchun dispetcher
dp = Dispatcher(bot)

# Botga jo'natilgan /start buyrug'ini qabul qilib olish uchun handler
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    # foydalanuvchiga javoban salom beradi
    await message.answer("Assalomu alaykum!")

# Foydalanuvchilardan kelgan matnni(textni) qabul qilib olish uchun handler
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    # Foydalanuvchi jo'natgan matnga javoban jo'natgan matnini o'ziga yuboradi
    await message.reply(message.text)


if __name__ == '__main__':
    # Botimizni ishga tushiramiz
    executor.start_polling(dp,skip_updates=True)
```
> API_TOKEN o'rniga @BotFather jo'natgan botimizning Tokenini qo'yamiz.

Keling endi yuqoridagi kodga biroz to'xtalib o'tsak:

E'tibor bergan bo'lsangiz aiogram asinxron([async](https://docs.python.org/3/library/asyncio-task.html "async haqida ma'lumot")) kutubxona hisoblanadi. Shuning uchun funksiyadan oldin ```async```, [Telegram Bot API](https://core.telegram.org/bots/api "Telegram Bot API")'dagi metodlarga murojaat qilishdan avval esa ```await``` qo'shib yoziladi.

Foydalanuvchidan kelayotgan xabarlarni "ushlab" olish uchun [dekoratordan](https://mohirdev.uz/pythonda-decoratorlar/ "Dekorator haqida ma'lumot") foydalaniladi va handler yoziladi, handlerning ichiga esa sharti yoziladi. Handler'ning ichidagi sharti bizga foydalanuvchidan kelayotgan xabarni tekshirishga, agar biz yozgan shartga to'g'ri kelsa tagidagi funksiyaga o'tkazib yuborishi uchun kerak bo'ladi.

Hozir shunchaki yuzaki tushuntirdik, kursimiz davomida InshaAlloh ko'proq tushunchaga ega bo'lasiz. Keling endi yoqiridagi kodni run qilib ko'ramiz, agar botimiz muvaffaqiyatli ishga tushirilsa terminalga run qilganimizdan shunga o'xshash yozuv chiqadi:
```console
INFO:aiogram:Bot: TexnoKun.Uz uchun [@TexnoKunUzBot]
WARNING:aiogram:Updates were skipped successfully.
INFO:aiogram.dispatcher.dispatcher:Start polling.
```
Botimiz muvaffaqiyatli ishga tushganidan so'ng keling uni ishlatib ko'ramiz:
![1_dars_4](/images/1_dars_4.png)

Biz siz bilan foydalanuvchi ```/start``` buyrug'ini jo'natsa unga **Assalomu alaykum!** deb xabar jo'natadigan va har qanday matnli xabar jo'natsa, usha matnli xabarini o'ziga javoban qaytaradigan kichik bot qildik. Shu o'rinda aytib o'tish kerakki ```/start```ga bot bizga jo'natgan xabar **oddiy xabar** hisoblanadi, har-qanday matn jo'natsak bizning xabarimizga javoban jo'natgani esa **reply xabar** hisoblanadi. 

# **Xabarlar bilan ishlash**
### Matnlarni farmatlash <br>
Telegram bot orqali foydalanuvchilarga jo'natilayotgan xabarlarni formatlab jo'natish imkoniyati mavjud bo'lib, textlarni ajralib turadigan va chiroyliroq qilib jo'natish imkonini beradi. Ushbu formatlash bizga botimiz orqali foydalanuvchilarga **bold**, _italic_, <u>underline</u>, <s>strikethrough</s>, `code`, [url](# "havola") va spoiler(ustiga bosilmagunigacha ko'rinmaydigan) ko'rinishidagi matnlarni jo'nata olamiz. Formatlash uchun 3xil format mavjud: HTML, Markdown va MarkdownV2. Bulardan asosan foydalanadiganlar HTML va Markdown2 hisoblanadi. Shuning uchun biz siz bilan shu ikki usulda matnlarni formatlab jo'natishni ko'rib chiqamiz. Quyidagi kodni birinchi bo'limda yozgan kodimizga `/start` uchun yozilgan handler'dan kegin qo'shib olamiz:
```python
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
```

E'tibor bergan bo'lsangiz biz `answer()` funksiyasiga faqatgina text argumentini emas,balki `parse_mode` argumentini ham qo'shdik,ushbu argument orqali biz Telegram'ga matnimizni qaysi formatda formatlash kerakligini ko'rsatamiz.

Keling endi kodimizni ishga tushirib, botimizni sinab ko'ramiz:

![2_dars_1](/images/2_dars_1.png)

> To'liq kod: [havola](https://github.com/RDev-Uz/BotDarslari/blob/main/code/2dars_1.py)

Matnlarni formatlash bo'yicha to'liqroq quyidagi havola orqali tanishib chiqishingiz mumkin: [havola](https://core.telegram.org/bots/api#formatting-options)

### Media fayllar

Telegram Bot orqali nafaqat matnlar bilan ishlash, shu bilan bir qatorda rasmlar,  giflar, videolar, audiolar, stickerlar, geolokatsiyalar va hokazolar bilan ishlash mumkin. Ko'plab media fayllar o'zining `file_id` va `file_unique_id`siga ega. `file_id` bitta mediafaylni ko'p martta tezkor yuborish uchun foydalanilishi mumkin. Tezkor yuborish mumkinligining sababi ushbu fayl allaqachon Telegram serverlarida mavjudligidur. Botlarda mediafayllarni yuborish uchun ushbu usuldan foydalanish tavsiya etiladi.
