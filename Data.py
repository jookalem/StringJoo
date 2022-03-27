from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴀʟᴏ ɴɢᴇɴᴛᴏᴅ {} 😈

ᴡᴇʟᴋᴀᴍ ᴛᴏ {} 🤗

ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴇʀᴄᴀʏᴀɪ ʙᴏᴛ ɪɴɪ, 
𝟷> ɢᴀᴜsᴀ ʙᴀᴄᴀ ᴄʜᴀᴛ ɪɴɪ ʙɢᴇɴᴛᴏᴅ
𝟷> ʙʟᴏᴋɪʀ ʙᴏᴛ ᴀᴛᴀᴜ ᴅᴇʟᴇᴛᴇ ᴄʜᴀᴛ ɴɢᴇɴᴛᴏᴅ

ʙᴏᴛ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀɴᴛᴜ ᴋᴀᴍᴜ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴠɪᴀ ʙᴏᴛ. ʀᴇᴋᴏᴍᴇɴᴅᴀsɪ ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ɢᴜɴᴀᴋᴀɴ ᴀᴋᴜɴ ʟᴀɪɴ, ᴀɢᴀʀ ᴛɪᴅᴀᴋ ᴅᴇʟᴀʏ. ᴛᴇʀɪᴍᴀᴋᴀsɪʜ
ʙʏ @ikhsanntarjo
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 ᴍᴜʟᴀɪ sᴛʀɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 ᴍᴜʟᴀɪ sᴛʀɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 ᴍᴜʟᴀɪ sᴛʀɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ", url="https://t.me/ikhsanntarjo")],
        [
            InlineKeyboardButton("ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴғᴏ ʙᴏᴛ ʟᴀɪɴ", url="https://t.me/JoniSupport")],
    ]

    # Help Message
    HELP = """
✪ **Available Commands** ✪

/about - ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ
/help - ʙᴀɴᴛᴜᴀɴ
/start - ᴍᴜʟᴀɪ ʙᴏᴛ
/generate - ᴍᴜʟᴀɪ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ
/cancel - ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs
/restart - ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs
"""

    # About Message
    ABOUT = """
✪ **About This Bot** ✪

sᴇʙᴜᴀʜ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘʏʀᴏɢʀᴀᴍ ᴅᴀɴ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @joostringbot

Group Support : [ɢᴀʙᴜɴɢ](https://t.me/JoniSupport)

Framework : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Language : [ᴘʏᴛʜᴏɴ](www.python.org)

Developer : @ikhsanntarjo
    """
