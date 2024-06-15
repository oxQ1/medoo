#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @UJ_5Q
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ox_Q1
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @U7_4K
#MOHAMED تم التعديل بواسطة 🎸 ⋅

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b56c2f4ff37d1f22dd38a.jpg",
        caption=f"""مرحبا بك عزيزي في اوامر بوت الميوزك 🎸 ⋅\n- اسمك : {message.from_user.mention} 💘 ⋅\n- عليك استخدام الازرار بالاسفل لتصفح اوامر الميوزك 🎸 ⋅ \n\n• ⌯ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎 ⌯ • </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ⌯ اوامر التشغيل ⌯ •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• ⌯ اوامر القناة ⌯ •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• ⌯ اوامر الادمن ⌯ •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• ⌯ اوامر المطور ⌯ •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎", url="https://t.me/UJ_5Q"),
                ],
            ]
        ),
    )
      
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @UJ_5Q
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @ox_Q1
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @U7_4K
#MOHAMED تم التعديل بواسطة 🎸 ⋅

