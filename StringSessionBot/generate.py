from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "Oops! An exception occurred! \n\n**Error** : {} " \
            "\n\nTolong Laporan ke [Support](t.me/NastySupportt) jika eror " \
            "sensitive information and you if want to report this as " \
            "this error message is not being logged by us!"


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(
        "sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ sᴛʀɪɴɢ ᴍᴀɴᴀ ʏᴀɴɢ ɪɴɢɪɴ ᴋᴀᴍᴜ ᴀᴍʙɪʟ 🤗",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram"),
            InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply("ᴍᴇᴍᴜʟᴀɪ {} sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴘɴ...".format("Telethon" if telethon else "Pyrogram"))
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ  `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('API_ID ᴛɪᴅᴀᴋ ʙᴇɴᴀʀ (which must be an integer). ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ `API_HASH`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(user_id, 'sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ `PHONE_NUMBER` ᴅᴇɴɢᴀɴ ᴋᴏᴅᴇ ɴᴏᴍᴏʀ. \nExample : `+628xxxxxxx`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("Sending OTP...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` and `API_HASH` combination is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` sᴀʟᴀʜ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "sɪʟᴀʜᴋᴀɴ ᴘᴇʀɪᴋsᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴅɪ ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ, ᴊɪᴋᴀ ᴀᴅᴀ, sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ ᴋᴇ sɪɴɪ sᴇᴛᴇʟᴀʜ ᴍᴇᴍʙᴀᴄᴀ ғᴏʀᴍᴀᴛ ᴅɪʙᴀᴡᴀʜ ɪɴɪ. \nᴊɪᴋᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴀᴅᴀʟᴀʜ 12345, sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍ 1 2 3 4 5..", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply('ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ᴍᴇɴᴄᴀᴘᴀɪ 10 ᴍᴇɴɪᴛ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('ᴏᴛᴘ ɪs ɪɴᴠᴀʟɪᴅ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('ᴏᴛᴘ ɪs ɪɴᴠᴀʟɪᴅ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴠᴇʀɪᴠɪᴋᴀsɪ ᴅᴜᴀ ʟᴀɴɢᴋᴀʜ. ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴋᴀᴛᴀ sᴀɴᴅɪɴʏᴀ.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ᴍᴇɴᴄᴀᴘᴀɪ 5 ᴍᴇɴɪᴛ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('ᴋᴀᴛᴀ sᴀɴᴅɪ sᴀʟᴀʜ. ᴍᴏʜᴏɴ ᴀᴍʙɪʟ sᴛʀɪɴɢ ᴜʟᴀɴɢ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = "**{} STRING SESSION** \n\n`{}` \n\nGenerated by @joostringbot".format("TELETHON" if telethon else "PYROGRAM", string_session)
    await client.send_message("me", text)
    await client.disconnect()
    await phone_code_msg.reply("ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴍʙɪʟ {} sᴛʀɪɴɢ sᴇssɪᴏɴ. \n\sɪʟᴀʜᴋᴀɴ ᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ. \n\nʙʏ @ikhsanntarjo".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ ʙᴏᴛ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!", quote=True)
        return True
    else:
        return False


# @Client.on_message(filters.private & ~filters.forwarded & filters.command(['cancel', 'restart']))
# async def formalities(_, msg):
#     if "/cancel" in msg.text:
#         await msg.reply("ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏsᴇs!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     elif "/restart" in msg.text:
#         await msg.reply("ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ ʙᴏᴛ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     else:
#         return False
