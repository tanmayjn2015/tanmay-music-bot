# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

import random

from pyrogram import filters
from pyrogram.types import Message

from TANMAYMUSIC import app
from TANMAYMUSIC.misc import db
from TANMAYMUSIC.utils.decorators import AdminRightsCheck
from TANMAYMUSIC.utils.colored_buttons import (
    buttons_to_inline_markup,
    smart_send_message as send_message_colored,
    smart_edit_message_text as edit_message_text_colored,
    edit_reply_markup_colored,
)
from TANMAYMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await send_message_colored(chat_id=message.chat.id, text=_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await send_message_colored(chat_id=message.chat.id, text=_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await send_message_colored(chat_id=message.chat.id, text=_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await send_message_colored(chat_id=message.chat.id, 
        text=_["admin_16"].format(message.from_user.mention),
        reply_markup=close_markup(_)
    )

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
