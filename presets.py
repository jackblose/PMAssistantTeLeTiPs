class Presets(object):
    WELCOME_TEXT = "Hai, <b>{}</b>\n<code>Saya Adalah Asisten Della Cantik\nKirim pesan kamu ke della disini👇🏻</code> "
    USER_DETAILS = "<b>PM FROM:</b>\nName: {} {}\nId: {}\nUname: @{}\nScam: {}\nRestricted: {}\nStatus: {}\nDc Id: {}"
    PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
    PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

@register(outgoing=True, pattern='^/start(?: |$)(/*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ᴀsᴜᴘᴀɴ ʙᴇʀɢɪᴢɪ = [ᴛᴇᴋᴀɴ ᴅɪsɪɴɪ](https://t.me/joinchat/HqzBMqat6SszOGQ1)")

# Thakshaka Rathnayake - TeLe TiPs
# ©️2021 TeLe TiPs All Rights Reserved
