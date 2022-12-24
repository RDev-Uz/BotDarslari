# Telegram bot tuzamiz! (Python dasturlash tilida)

Ushbu maqolamizda biz siz bilan python dasturlash tilida qanday qilib telegram bot tuzish mumkinligini ko'rib chiqamiz. Buning uchun sizga python dasturlash tilini kamida boshlang'ich darajada bilish va Telegram Botni tuzishni o'rganish uchun xohish kerak bo'ladi.

Telegram botni aslida barcha https so'rov yuborsa bo'ladigan dasturlash tillarida tuzsa bo'ladi(Php, Go, Python, Rust, JavaScript(Node.JS), Java va [boshqalar](https://core.telegram.org/bots/samples)). Biz Python dasturlash tilida telegram bot tuzishni ko'ramiz, buning sababi esa hozirda ushbu ommalashgan va o'rganishga oson dasturlash tilaridan biri. 

Keling avval barcha botlar qanday ishlashini bilib olsak:

Barcha botlar [Telegram Bot API](https://core.telegram.org/bots/api)'dagi metodlar orqali ishlaydi. [Telegram Bot API](https://core.telegram.org/bots/api)'da qanday metodlar borligi va ularning argumentlari bilan tanishib chiqishingiz mumkin.

Telegram Botni dasturlash oson bo'lishi uchun Python dasturlash tilida ko'plab kutubxonalar(modullar) mavjud bo'lib,ulardan eng mashhurlari [aiogram](https://github.com/aiogram/aiogram), [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot), [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) hisoblanadi.

Biz Telegram Botni dasturlash uchun [Aiogram](https://github.com/aiogram/aiogram) kutubxonasidan foydalanamiz. Quyida ushbu kutubxonaning boshqalaridan ustun jihatlari bilan tanishishingiz mumkin: 

- Asinxronligi([async](https://en.wikipedia.org/wiki/Async/await)); 
- Telegram Bot API'dagi yangi metodlar/o'zgarishlar tezkor qo'shilishi bilan;
- Katta community(jamoa) tomonidan qo'llab-quvvatlanishi;
- O'rganish va muammolarni bartaraf etish uchun ko'plab manbalar mavjudligi.
----------
![1-dars-pypi.org](images/2_dars_pypi.png)

Hozirda aiogramning eng oxirgi versiyasi 2.23.1([2.x](https://docs.aiogram.dev/en/latest/)) hisoblanadi. Bundan tashqari aiogramning [3.x](https://docs.aiogram.dev/en/dev-3.x/) versiyasi ham bor,u hozirda beta(sinov) versiya bo'lganligi uchun aiogramning [2.x](https://docs.aiogram.dev/en/latest/) versiyasidan foydalanishga qaror qildik.


Botni kodini yozishga kirishishdan oldin [vertual muhut](https://docs.python.org/3/library/venv.html)(venv) yaratib olamiz:
```console
python3 -m venv venv
```
Yaratgan vertual muhutimizni aktivlashtirib olamiz.

Windows:
```console
venv\Scripts\activate.bat

```
Linux:
```console
source venv/bin/activate
```
