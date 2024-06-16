import asyncio

import os

import time

import requests

import aiohttp

import config

from pyrogram import filters

from pyrogram import Client

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

from MatrixMusic import app



import re

import sys

from os import getenv



from dotenv import load_dotenv



load_dotenv()



OWNER_ID = getenv("OWNER_ID")



OWNER = getenv("OWNER")





def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj



@app.on_message(filters.command(["المطور"], ""))

async def khfzss(client: Client, message: Message):

    usrr = await client.get_chat(OWNER_ID)

    name = usrr.first_name

    bio = usrr.bio

    id = usrr.id

    username = usrr.username

    async for photo in client.get_chat_photos(OWNER_ID, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""مـعـلـومـات مـطـور الـبـوت 🌿  \n\n⌔︙𝐍𝐚𝐦𝐞: {name} \n\n⌔︙𝐔𝐬𝐢𝐫: @{username} \n\n⌔︙𝐢𝐝: {id} \n\n⌔︙𝐁𝐢𝐨: {bio} \n\n⌔︙𝐒𝐎𝐔𝐑𝐂𝐄 𝐄𝐑𝐎𝐑""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, url=f"https://t.me/{username}")

                ],

            ]

        ),

    )                    

                    sender_id = message.from_user.id

                    sender_name = message.from_user.first_name

                    await app.send_message(OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")

                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")



