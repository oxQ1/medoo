from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="خدني لجروبك ونبي🥺💕", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="جـروب الـدعـم 🌿 ", url= "https://t.me/SOPER_EROR"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="خدني لجروبك ونبي🥺💕",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مـطـور الـسـورس 🌿 ", url= "https://t.me/Y_D_ll"),
            InlineKeyboardButton(text="جـروب الـدعـم 🌿 ", url=f"https://t.me/SOPER_EROR"), 
        ],
        [
            
            InlineKeyboardButton(text="قـنـاة الـسـورس 🌿 ", url=f"https://t.me/SOURCE_EROR") , 
        ],
    ]
    return buttons
