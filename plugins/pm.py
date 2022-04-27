import os
import asyncio
import logging
from pyrogram import Client, filters
from Script import script
from info import CHANNELS, ADMIN, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PM
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.users_chats_db import db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@Client.on_message(filters.private & filters.text)
async def pm_text(client: Client, message):
    try:
        if message.from_user.id == ADMIN:
            await reply_text(client, message)
            return
                   
        info = await client.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)

        await db.add_user(message.from_user.id, message.from_user.first_name)
     
        k = await client.send_message(
            chat_id=ADMIN,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text, message.from_user.first_name),
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(f'ɪɴғᴏ', 'infos')
                            ],
                            [
                                InlineKeyboardButton("⚠️ Can't Access ❓ Click Here ⚠️", url=f'https://t.me/+Md9dwytUK1NhNTc9')
                            ],                       
                            [
                                InlineKeyboardButton('📥 Download 📥 ', url = "https://t.me/NasraniMovies")
                            ]
                        ]
                    )
                )
        await asyncio.sleep(180)
        await k.delete()
        await client.send_message(
            chat_id=PM,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(f'ɪɴғᴏ', 'infos')
                            ],
                            [
                                InlineKeyboardButton("⚠️ Can't Access ❓ Click Here ⚠️", url=f'https://t.me/+Md9dwytUK1NhNTc9')
                            ],                       
                            [
                                InlineKeyboardButton('📥 Download 📥 ', url = "https://t.me/NasraniMovies")
                            ]
                        ]
                    )
                )
    except Exception as e:
        logger.exception(e)


# @Client.on_message(filters.private & filters.media)
# async def pm_media(bot, message):
#     if message.from_user.id in ADMINS:
#         await replay_media(bot, message)
#         return
#     info = await bot.get_users(user_ids=message.from_user.id)
#     reference_id = int(message.chat.id)
#     await bot.copy_message(
#         chat_id=ADMINS,
#         from_chat_id=message.chat.id,
#         message_id=message.message_id,
#         caption=script.PM_MED_ATT.format(reference_id, info.first_name),
#         parse_mode="html"
#     )


@Client.on_message(filters.private & filters.user(ADMIN) & filters.text & filters.reply)
async def reply_text(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.send_message(
                text=message.text,
                chat_id=int(reference_id),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(f'ɪɴғᴏ', 'infos')
                        ],
                        [
                            InlineKeyboardButton("⚠️ Can't Access ❓ Click Here ⚠️", url=f'https://t.me/+Md9dwytUK1NhNTc9')
                        ],                       
                        [
                            InlineKeyboardButton('📥 Download 📥 ', url = "https://t.me/NasraniMovies")
                        ]
                    ]
                )
            )
    except Exception as e:
        logger.exception(e)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.media & filters.reply)
async def replay_media(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.copy_message(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.message_id,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(f'ɪɴғᴏ', 'infos')
                        ],
                        [
                            InlineKeyboardButton("⚠️ Can't Access ❓ Click Here ⚠️", url=f'https://t.me/+Md9dwytUK1NhNTc9')
                        ],                       
                        [
                            InlineKeyboardButton('📥 Download 📥 ', url = "https://t.me/NasraniMovies")
                        ]
                    ]
                )
            )
    except Exception as e:
        logger.exception(e)
