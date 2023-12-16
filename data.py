from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🎉 Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ 🧸", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🍷 Rᴇᴛᴜʀɴ Hᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🐣 Fᴇᴇʟɪɴɢs 🍂", url="https://t.me/Soul_x6")],
        [
            InlineKeyboardButton("Hᴏᴡ Tᴏ Usᴇ ❔", callback_data="help"),
            InlineKeyboardButton("🥀 ᴀʙᴏᴜᴛ 🦋", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Mʀ. Dʜɪᴍᴀɴ ♥", url="https://t.me/i_dxlvir")],
    ]

    START = """
Hey {}

Welcome to {}

ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ, 
1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ

ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

Bʏ : @Abt_Mei
    """

    HELP = """
✨ **Aᴠᴀɪʟᴀʙʟᴇ Cᴍᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍsɢ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ! 
/generate - ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    ABOUT = """
**Aʙᴏᴜᴛ Dʜɪᴍᴀɴ Sᴛʀɪɴɢ Sᴇssɪᴏɴ Bᴏᴛ** 

Tᴇʟᴇɢʀᴀᴍ Bᴏᴛ Tᴏ Gᴇɴᴇʀᴀᴛᴇ Pʏʀᴏɢʀᴀᴍ Aɴᴅ Tᴇʟᴇᴛʜᴏɴ Sᴛʀɪɴɢ Sᴇssɪᴏɴ Bʏ : @i_dxlvir

🌸 sᴜᴘᴘᴏʀᴛ : [Dʜɪᴍᴀɴ Dɪsᴄᴜs](https://t.me/PUNJABI_HINDI_CHAT)

🌸 ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

🌸 ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](https://www.python.org)

🍂 ᴅᴇᴠᴇʟᴏᴘᴇʀ : @i_dxlvir
    """
