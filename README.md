# **Telegram bot tuzishni o'rganamiz**


Assalomu Alaykum. Ushbu kursimizda siz bilan python dasturlash tilida, aiogram frameworkida Telegram Bot tuzishni o'rganamiz. 

Aiogram python dasturlash tilida Telegram Bot yozish uchun eng mashhur frameworklardan biri hisoblanadi. Ushbu framework ham boshqa Telegram Bot tuzish uchun mo'ljallangan kutubxona/framework lar kabi [Telegram Bot API](https://core.telegram.org/bots/api)'dan kelayotgan yangilanishlarni olish ([GetUpdates](https://core.telegram.org/bots/api#getupdates)) va foydalanuvchilarga javob qaytarish uchun ishlab chiqilgan bo'lib,katta jamoa(community) tomonidan rivojlantirib kelinmoqda.

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
- Ketma-ketlik bo'yicha foydalanuvchidan ma'lumotlarni qabul qilish(FSM);

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
Keling avval bizga kerakli frameworkni, yani Aiogram'ni o'rnatib olamiz:
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

E'tibor bergan bo'lsangiz aiogram asinxron([async](https://docs.python.org/3/library/asyncio-task.html "async haqida ma'lumot")) framework hisoblanadi. Shuning uchun funksiyadan oldin ```async```, [Telegram Bot API](https://core.telegram.org/bots/api "Telegram Bot API")'dagi metodlarga murojaat qilishdan avval esa ```await``` qo'shib yoziladi.

Foydalanuvchidan kelayotgan xabarlarni "ushlab" olish uchun [dekoratordan](https://mohirdev.uz/pythonda-decoratorlar/ "Dekorator haqida ma'lumot") foydalaniladi va handler yoziladi, handlerning ichiga esa sharti yoziladi. Handler'ning ichidagi sharti bizga foydalanuvchidan kelayotgan xabarni tekshirishga, agar biz yozgan shartga to'g'ri kelsa tagidagi funksiyaga o'tkazib yuborishi uchun kerak bo'ladi.

Hozir shunchaki yuzaki tushuntirdik, kursimiz davomida InshaAlloh ko'proq tushunchaga ega bo'lasiz. Keling endi yuqoridagi kodni run qilib ko'ramiz, agar botimiz muvaffaqiyatli ishga tushirilsa terminalga run qilganimizdan shunga o'xshash yozuv chiqadi:
```console
INFO:aiogram:Bot: TexnoKun.Uz uchun [@TexnoKunUzBot]
WARNING:aiogram:Updates were skipped successfully.
INFO:aiogram.dispatcher.dispatcher:Start polling.
```
Botimiz muvaffaqiyatli ishga tushganidan so'ng keling uni ishlatib ko'ramiz:
![1_dars_4](/images/1_dars_4.png)

Biz siz bilan foydalanuvchi ```/start``` buyrug'ini jo'natsa unga **Assalomu alaykum!** deb xabar jo'natadigan va har qanday matnli xabar jo'natsa, usha matnli xabarini o'ziga javoban qaytaradigan kichik bot qildik. Shu o'rinda aytib o'tish kerakki ```/start```ga bot bizga jo'natgan xabar **oddiy xabar** hisoblanadi, har-qanday matn jo'natsak bizning xabarimizga javoban jo'natgani esa **reply xabar** hisoblanadi. 

# **Xabarlar bilan ishlash**
### Matnlarni formatlash <br>
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

Matnlarni formatlash bo'yicha to'liqroq quyidagi havola orqali tanishib chiqishingiz mumkin: [havola](https://core.telegram.org/bots/api#formatting-options).

Aiogramning `Bot` classida `parse_mode` argumenti bo'lib, ushbu argument orqali biz oson qaysi format turida formatlash kerakligini bera olamiz, masalan:
```python
bot = Bot("BOT_TOKEN",parse_mode=types.ParseMode.HTML)
```

### Media fayllar

Telegram Bot orqali nafaqat matnlar bilan ishlash, shu bilan bir qatorda rasmlar,  giflar, videolar, audiolar, stickerlar, geolokatsiyalar va hokazolar bilan ishlash mumkin. Barcha media fayllar o'zining `file_id` va `file_unique_id`siga ega. `file_id` bitta mediafaylni ko'p martta tezkor yuborish uchun foydalanilishi mumkin. Tezkor yuborish mumkinligining sababi ushbu fayl allaqachon Telegram serverlarida mavjudligidur. Botlarda media fayllarni yuborish uchun ushbu usuldan foydalanish tavsiya etiladi. Masalan, quyidagi kod foydalanuvchidan kelgan animatsiya'ni o'ziga bir zumda `file_id`si orqali qaytaradi:

```python
# Foydalanuvchidan kelayotgan sticker'ni "ushlab" olish uchun handler
@dp.message_handler(content_types=['sticker'])
async def return_anim(message: types.Message):
    # Foydalanuvchi jo'natgan stickerga javoban jo'natilgan stickerni qaytaradi
    await message.reply_sticker(message.sticker.file_id)
```
Natija:
![1_dars_2](/images/2_dars_2.png)

> `file_id` har bir Telegram Bot uchun unikal bo'ladi, yani bitta bot orqali olingan `file_id` boshqa bot uchun ishlamaydi. `file_unique_id` esa biror bir media fayl uchun boshqa botlarda ham o'zgarmas identifikator hisoblanadi, `file_unique_id` orqali mediafayllarni jo'natib bo'lmaydi.
----------
Aiogramda foydalanuvchidan kelgan media fayllar va fayllarni yuklash uchun `download()` funksiyasi mavjud,namuna uchun kod:
```python
# Foydalanuvchidan kelgan faylni "ushlab" olish uchun handler
@dp.message_handler(content_types=['document'])
async def down_doc(message: types.Message):
    # Bot ishga tushirilgan direktoriyaga faylni yuklaydi
    await message.document.download()
    await message.reply("✅ Fayl muvaffaqiyatli yuklandi!")


# Foydalanuvchidan kelgan rasmni "ushlab" olish uchun handler
@dp.message_handler(content_types=["photo"])
async def down_photo(message: types.Message):
    # Bot ishga tushirilgan diroktoriyadagi images nomli papkaga rasmni yuklaydi.
    await message.photo[-1].download()
    await message.reply("✅ Rasm muvaffaqiyatli yuklandi!")
```
> E'tibor bergan bo'lsangiz biz rasmni yuklashda `message.photo[-1]` qildik. Buning sababi foydalanuvchi botga rasm yuborganida Telegram bizga bitta `photo` obyektida foydalanuvchi jo'natgan rasmnining har-xil sifatdagisini yuboradi, eng oxirgisi eng sifatlisi hisoblanadi, shuning uchun biz eng oxirgi elementni, yani eng sifatli rasmning `file_id`sini `[-1]` orqali olamiz va yuklaymiz.

# **Tugmalar bilan ishlash**

Ushbu bo'limda biz siz bilan Telegram Botdagi tugmalar bilan ishlashni o'rganamiz. Telegram bot ikki xil tugmani jo'nata oladi: **oddiy** va **inline**(inlayn). Oddiy tugma deb ekranning past qismida chiqadigan tugmaga aytiladi, inline deb esa xabarning tagida chiqadigan tugmaga, quyidagi rasmda farqlarini ko'rishingiz mumkin:

![3_dars_1](/images/3_dars_1.png)

## **Oddiy tugmalar**

Oddiy tugma bosilganida unda yozilgan matn hudda foydalanuvchi jo'natgan matndek chatga jo'natiladi. Ushbu tugma bosilganida foydalanuvchiga javob berish uchun biz matnni qabul qiladigan handler yozishimiz kerak. Keling foydalanuvchi `/start` buyrug'ini yuborsa matnli xabar bilan oddiy tugma jo'natamiz:

```python
# from aiogram import types

@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup() # keyboard obyekti
    keyboard.add(types.KeyboardButton(text="Yaxshi")) # keyboardga KeyboardButton() orqali tugma qo'shish
    keyboard.add("Yomon") # KeyboardButton()'siz keyboardga tugma qo'shish
    await message.answer("Kayfiyatingiz qanday?", reply_markup=keyboard)
```
> E'tibor bergan bo'lsangiz "Yomon" tugmasini biz `KeyboardButton()`siz qo'shdik, chunki yangi tugma qo'shish uchun `add()` funksiyasiga shunchaki tugma uchun matnni bersa ham bo'ladi.

Keling endi kodimizni ishga tushirib, natijani ko'ramiz:

![3_dars_2](/images/3_dars_2.png)

Ko'rib turganingizdek ikkita tugma chiqdi, biroq tugmalarimiz kattaroq. Tugmalarni kichraytirish uchun keyboard obyektiga `resize_keyboard=True` parametrini berish kerak. Keling bira to'lasi ikkita tugmani bitta qatorda chiqarishni ham ko'ramiz. Keling endi kodimizni biroz o'zgartirib, yuqoridagilarni kodimizda qo'llaymiz:

```python
@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # keyboard obyekti
    buttons = ['Yaxshi','Yomon']
    keyboard.add(*buttons) # yoki .add('Yaxshi','Yomon')
    await message.answer("Kayfiyatingiz qanday?", reply_markup=keyboard)
```

Endi kodni qayta ishga tushirib, natijani ko'ramiz:

![3_dars_3](/images/3_dars_3.png)

Ko'rib turganingizdek tugmalar kichyardi va bir qatorda bo'ldi.

Ushbu tugmalarni foydalanuvchi bosganda unga javob beradigan qilish qoldi. Yoqorida aytib o'tganimizdek foydalanuvchi oddiy tugmani bosganida ushbu tugma botga matndek keladi, shuning uchun biz **Yaxshi** va **Yomon** matnlarini handlerda "ushlab" olishimiz kerak. Ma'lum bir matnni "ushlab" olish uchun handlerda aiogram'da `Text` filteri mavjud:
```python
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text("Yaxshi")) # yoki text="Yaxshi"
async def good(message: types.Message):
    await message.reply("Kayfiyatingiz yaxshi ekanligidan xursandman :)")

@dp.message_handler(Text("Yomon"))
async def bad(message: types.Message):
    await message.reply("Kayfiyatingiz yomonligidan afsusdaman :(\nSizga yaxshi kayfiyat tilab qo'laman!")
```

Kodimizni qayta ishga tushirib, natijasini ko'ramiz: 

![3_dars_4](/images/3_dars_4.png)

E'tibor bergan bo'lsangiz biz tugmani bosganimizdan so'ng ham tugmalar o'chmayapti. Ushbu tugmalarni o'chirish uchun `ReplyKeyboardRemove` mavjud. Qo'llash uchun misol:
```python
await message.reply("Kayfiyatingiz yaxshi ekanligidan xursandman :)",reply_markup=types.ReplyKeyboardRemove())
```

> Siz bilan to'liq bo'lmasa ham [oddiy tugmalar](https://core.telegram.org/bots/api#replykeyboardmarkup) bilan ishlashni o'rgandik. Agar to'liqroq o'rganmoqchi bo'lsangiz manbalar: (Telegram Bot API: [ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup), [KeyboardButton](https://core.telegram.org/bots/api#keyboardbutton)), (Aiogram Docs: [ReplyKeyboardMarkup](https://docs.aiogram.dev/en/latest/telegram/types/reply_keyboard.html?highlight=replykeyboardmarkup#replykeyboardmarkup), [KeyboardButton](https://docs.aiogram.dev/en/latest/telegram/types/reply_keyboard.html?highlight=replykeyboardmarkup#keyboardbutton)).

## Maxsus oddiy tugmalar

Oddiy tugmalarning vazifasi faqatgina foydalanuvchi biror bir tugmani bossa, usha tugma matnini chatga jo'natishdan iborat emas. Balki oddiy tugmalar orqali foydalanuvchining joylashuvini,telefon raqamini qabul qilish mumkin. Keling ushbu tugmalarni kodda qanday bo'lishini ko'ramiz:
```python
@dp.message_handler(commands="buttons")
async def buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Lokatsiyani yuborish", request_location=True))
    keyboard.add(types.KeyboardButton(text="Telefon raqamni yuborish", request_contact=True))
    await message.answer("Quyidagi maxsus tugmalardan birini tanlang: ", reply_markup=keyboard)
```

> Oddiy tugmalar bilan ishlashda yozilgan to'liq kod: [havola](https://github.com/RDev-Uz/BotDarslari/blob/main/code/2dars.py)

## **Inline(inlayn) tugmalar**

Inline(inlayn) tugmalar yuborilgan xabarning tagida chiqadi, oddiy tugmalar kabi ekranning pastgi qismida emas. Biz siz bilan ikki xil turdagi inline tugmalar bilan ishlashni o'rganamiz,bular: url va callback.

## URL(havolali) tugmalar

Ushbu turdagi tugmalar orqali foydalanuvchi biror `http(s)` yoki `tg://` bilan boshlangan havolalarga yo'naltirsa bo'ladi.
```python
@dp.message_handler(commands='url_tugma')
async def url_tugma(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Instagram",url="https://www.instagram.com/texnokun_uz/"),
        types.InlineKeyboardButton(text="Telegram kanal",url="tg://resolve?domain=texnokun_uz"),
    ]
    keyboard.add(*buttons)
    await message.answer("TexnoKun.uz'ning ijtimoiy tarmoqlardagi sahifasi: ",reply_markup=keyboard)
```

Natija esa:

![3_dars_5](/images/3_dars_5.png)

Agar ikkita tugmani bir qatorda qilmoqchi bo'lsangiz `InlineKeyboardMarkup`dan `row_width=1`ni olib tashlang(shunda standart(default) qiymat 3 ishlatiladi). `row_width` parametri orqali bir qatorda nechta tugma bo'lishi kerakligini sozlash mumkin.

## Callback tugmalar

Callback tugmalarda foydalanuvchi qaysi tugmani bosganini bilish uchun o'zida maxsus qiymatni(data) saqlaydi. Ushbu qiymat bizga foydalanuvchi qaysi tugma bosganini va unga javoban nima deyish kerakligini bilish uchun kerak bo'ladi. Sodda qilib aytganda foydalanuvchi qaysi tugmani bosganini bilish va shunga qarab javob qaytarish uchun callback tugmalarda qiymat saqlanadi. 

Keling endi praktikaga o'tsak, foydalanuvchi botga `/random` buyrug'ini jo'natsa, unga callback tugma jo'natamiz:
```python
@dp.message_handler(commands='random')
async def random_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Tugmani bosing",callback_data='random_value'))
    await message.answer("1dan 10gacha bo'lgan tasodifiy sonlarni jo'natishim uchun quyidagi tugmani bosing: ", reply_markup=keyboard)
```
Endi ushbu tugmani bosganda foydalanuvchiga javob berish qoldi. Biror bir xabarni "ushlab" olish uchun avval biz `message_handler`dan foydalangan bo'lsak, callbackni "ushlab" olish uchun `callback_query_handler`dan foydalanamiz. Foydalanuvchi tugmani bosganida uni "ushlab" olish uchun biz tugmamizga bergan `callback_data`ni,yani maxsus qiymatni ushlab oladigan handler qilamiz:
```python
from random import randint

@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1,10)))
```

> `callback_query_handler`da ham `message_handler` kabi `text` filter qo'llaniladi.

![3_dars_6](/images/3_dars_6.png)

Keling yuqoridagi kodimizga biroz o'zgartirish kiritib, tasodifiy sonni jo'natmasdan, bot jo'natgan xabarini tahrirlab foydalanuvchiga tasodifiy sonni taqdir etamiz:
```python
@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.edit_text(str(randint(1,10)))
```
Endi callback tugmani bosganingizda xabarni tahrirlab, tasodifiy sonni taqdim etadi. Sinab ko'rishingiz mumkin.

> Callback tugmalar bilan ishlashdagi barcha kodlar: [link](https://github.com/RDev-Uz/BotDarslari/blob/main/code/3dars_2.py)

## **Ketma-ketlik bo'yicha foydalanuvchidan ma'lumotlarni qabul qilish(FSM)**

Tasavvur qilaylik siz botingizga ro'yxatdan o'tish qismini qo'shmoqchimiz,masalan foydalanuvchidan: ismi, jinsi va yoshini so'raydigan qilmoqchisiz. Shunday xolatlar uchun aiogramda [Finite state machine(FSM)](https://docs.aiogram.dev/en/latest/examples/finite_state_machine_example.html) mavjud.

Foydalanuvchi kiritgan ma'lumotlarni saqlash uchun aiogramdagi FSM'da turli-xil saqlash usullari mavjud,barchasini ro'yxati uchun: [link](https://github.com/aiogram/aiogram/tree/dev-2.x/aiogram/contrib/fsm_storage). Biz bugungi darsimizda [MemoryStorage](https://github.com/aiogram/aiogram/blob/dev-2.x/aiogram/contrib/fsm_storage/memory.py)'dan foydalanamiz. Ushbu usulda saqlangan ma'lumotlar operativ xotirada saqlanganligi bois **haqiqiy prayektlar uchun tavsiya etilmaydi**. 

Keling foydalanuvchidan ismi, familiyasi va yoshini so'raydigan va ro'yxatdan o'tish qismida **Bekor qilish** tugmasini bossa ro'yxatdan o'tishni bekor qiladigan kichik bot qilib ko'ramiz. Avval foydalanuvchidan kelgan qiymatlarni saqlash uchun `StatesGroup` class'dan meros bo'lgan class yaratib olamiz, uning ichida esa qabul qilishim kerak bo'lgan har bir qiymat uchun bitta o'zgaruvchi olib, u o'zgaruvchiga `State` classini qiymatlaymiz. Keling ushbu amallar uchun `states.py` nomli boshqa fayl ochib olamiz(chunarliroq va chiroyliroq bo'lishi uchun) va unga qiyidagilarni yozamiz:
```python
from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    ism = State()
    familiya = State()
    yosh = State()
```

Endi asosiy faylni, yani `main.py`ni yozishni boshlaymiz,foydalanuvchi `/start` buyrug'ini jo'natsa undan ismini kiritishini so'raymiz:
```python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import Form

logging.basicConfig(level=logging.INFO)


bot = Bot(token="API_TOKEN")
dp = Dispatcher(bot,storage=MemoryStorage()) # FSM uchun MemoryStorage'ni ulaymiz

def cancel_btn():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Bekor qilish")
    return keyboard

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await Form.ism.set()
    await message.answer(
        "Assalomu Alaykum!\n\nIsmingizni kiriting: ",
        reply_markup=cancel_btn(),
    )

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
```

Koddagi `await Form.ism.set()` orqali biz ismni qabul qilish kerakligini sozlaymiz, yani nimani qabul qilish kerakligini ko'rsatamiz. Endi foydalanuvchi ismini kiritsa "ushlab" oladigan handlerni qo'shamiz:
```python
@dp.message_handler(state=Form.ism)
async def get_ism(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text) # State'dagi ism qiymatini yangilaymiz
    await Form.next() # Kengi State'ga o'tkazamiz
    await message.answer(
        "Endi familiyangizni kiriting: ",
        reply_markup=cancel_btn(),
    )

```

`state.update_data()` orqali biz State'dagi qiymatlarni yangilaymiz, argumenti sifatida esa qaysi stateni yangilash kerak ekanligi va qiymati ko'rsatiladi (hozirda bizda `ism=message.text`). `Form.next()` esa kengi state'ga o'tkazish uchun kerak, yani familiyani qabul qiladigan state'ga. Endi foydalanuvchi familiyasini kiritsa "ushlab" oladigan handler yozamiz:

```python
@dp.message_handler(state=Form.familiya)
async def get_familiya(message: types.Message,state: FSMContext):
    await state.update_data(familiya=message.text)
    await Form.next() # Kengi State'ga,yani yoshga o'tkazamiz
    await message.answer(
        "Yaxshi, endi yoshingizni kiriting: ",
        reply_markup=cancel_btn(),
    )
```
Endi so'ngi qadam, yani foydalanuvchidan yoshini qabul qilish qoldi:
```python
@dp.message_handler(state=Form.yosh)
async def finish_state(message: types.Message,state: FSMContext):
    if message.text.isdigit() is False: # Agar foydalanuvchi matn jo'natsa
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
```

Yuqoridagi kodda ko'rishingiz mumkinki, foydalanuvchidan qabul qilingan ma'lumotlarni `state`ning `get_data()` funksiyasi orqali olsak bo'ladi. Uning ichidagi qiymatni esa kalit so'z orqali olamiz(hozirgi xolatda `data['ism']`). Shiningdek `get()` orqali ham olsa bo'ladi,masalan:  `data.get('ism')`. `state.finish()` esa stateni yakunlaydi va ichidagi foydalanuvchidan qabul qilingan qiymatlarni tozalaydi.

Endi keling, foydalanuvchi **Bekor qilish** tugmasini bossa state'ni yakunlaydigan handler yozamiz:
```python
@dp.message_handler(text="Bekor qilish",state='*')
async def cancel_state(message: types.Message,state: FSMContext):
    await message.answer(
        "Ro'yxatdan o'tish bekor qilindi!\n\n"
        "Qayta ro'yxatdan o'tmoqchi bo'lsangiz /start buyrug'ini jo'nating.",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await state.finish()
```
> Yuqoridagi kodni birinchi handlerdan keginga, yani `/start` buyrug'ini "ushlab" oladigan handlerdan pastga qo'yish kerak.

Endi ishga tushirib, botimizni ishlatib ko'ramiz:

![4_dars_1](/images/4_dars_1.png)

**Bekor qilish** tugmasini sinab ko'ramiz:

![4_dars_2](/images/4_dars_2.png)

Ko'rib turganingizdek muammosiz ishlamoqda.

> To'liq kod uchun: [link](https://github.com/RDev-Uz/BotDarslari/tree/main/code/4dars)

## **Maqola oxiri**

Ushbu maqolamizda biz siz bilan qanday qilib aiogram frameworkida Telegram bot tuzish bo'yicha kichik bo'lsada foydali bilimlarni ulashdik deb o'ylayman. To'g'ri, ushbu maqolada kamchiliklar va yetishmovchiliklar bo'lishi mumkin, ushbu kamchiliklar uchun uzur so'rayman. Ushbu kamchilik va yetishmovchiliklarda sizga [google](https://google.com) va [youtube](https://youtube.com) yaqindan yordam beradi deb o'ylayman. 


## Foydalanilgan manbalar: 
- [Aiogram Docs(Examples)](https://docs.aiogram.dev/en/latest/examples/index.html); 
- [MasterGroosha.github.io](https://mastergroosha.github.io/aiogram-2-guide/).

> Ushbu darslikda kod asosan bitta faylda yozildi (`main.py`). Kodingiz optimalroq, chunarliroq va chalkash bo'lmasligi uchun aiogramda botlarni yozishni optimallashtirish uchun tuzilgan maxsus shablon(template)dan foydalanish tavsiya etiladi. Ushbu shablonlar orasidan sizga ushbu shablonni tavsiya etaman: [link](https://github.com/Tishka17/tgbot_template).


## *E'tiboringiz uchun rahmat, maqola sizga foydali bo'ldi deb o'ylayman!*
