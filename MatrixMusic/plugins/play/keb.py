import asyncio
from pyrogram import Client, filters
from strings.filters import command
from MatrixMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "🧑🏻‍✈️︙اهلا بك عزيزي العضو ♥️\n\n اليـكـ كـيب الاعـضاء الـخاص بــ سـورس ايـرور"




REPLY_MESSAGE_BUTTONS = [
    [
        ("المطور"),
        ("مطور السورس")
    ],
    
    [
        ("السورس"),
        ("الاوامر")
    ],
    [
        ("استوري"),
        ("اقتباس")
    ],
   
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("نكته"),
        ("احكام")
    ],
    [
        ("متحركه"),
        ("انمي")
    ],
    [
        ("فيلم"),
        ("قران")
    ],    
    [
        ("انصحني"),
        ("لو خيروك")
    ],
    [
        ("نقشبندي"),
        ("عبدالباسط")
    ],
    [
        ("حروف"),
        ("سوال")
    ],
    [
        ("يوتيوب"),
        ("اذكار")
    ],
    [
        ("غنيلي"),
        ("تلاوات")
    ],
    [
        ("افاتار شباب"),
        ("افاتار بنات")
    ],
    [
        ("❎ ¦ حذف الكيبورد")
    ]
  
]



  

@app.on_message(filters.regex("^/medo"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("❎ ¦ حذف الكيبورد"))
async def down(client, message):
          m = await message.reply("❎ ¦ تم حذف الكيبورد بنجاح", reply_markup= ReplyKeyboardRemove(selective=True))

       
       
@app.on_message(filters.regex("يوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/b56c2f4ff37d1f22dd38a.jpg,
        caption=f"""يتم استخدام هذا الامر لعرض تحميل من اليوتيوب\nاستخدم الامر بهذا الشكل `تنزيل`  او  `يوتيوب`  كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدا """,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎", url=f"https://t.me/UJ_5Q"),
            ]
         ]
     )
        )
