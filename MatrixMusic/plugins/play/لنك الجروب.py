#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCE_EROR
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @Y_D_ll
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @SOPER_EROR
#MOHAMED تم التعديل بواسطة 🎸 ⋅

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic import app

@app.on_message(filters.command(["الرابط","/link","لنك","رابط"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("- ارفعني مسول الاول يزميلي 😂💘 ⋅")
    await message.reply_text(f"- تم جلب الرابط بنجاح 😂💘 ⋅\n {invitelink}")
    
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @SOURCE_EROR
#𝙳𝙴𝚅 𝙼𝙰𝚉𝙴𝙽 : @Y_D_ll
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @SOPER_EROR
#MOHAMED تم التعديل بواسطة 🎸 ⋅