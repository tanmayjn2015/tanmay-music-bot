# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

from pyrogram import filters
from TANMAYMUSIC import app
from config import OWNER_ID

destination_group_id = -1002425220992

@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(OWNER_ID))
async def copy_messages(_, message):

    if message.reply_to_message:

        await message.reply_to_message.copy(destination_group_id)
        await message.reply("ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ ")

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
