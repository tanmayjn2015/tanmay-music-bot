# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

import config
from TANMAYMUSIC import app
from TANMAYMUSIC.utils.colored_buttons import styled_button


def start_panel(_):
    # Add me = success (green, positive CTA), Channel = primary (blue, info)
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style="success"),
            styled_button(text=_["S_B_2"], url=config.SUPPORT_CHANNEL, style="primary"),
        ],
    ]
    return buttons


async def private_panel(_):
    # Add me = success (green CTA), Owner + Support = primary (blue), Help = success (green)
    owner_id = config.OWNER_ID
    buttons = [
        [
            styled_button(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style="success"),
        ],
        [
            styled_button(text=_["S_B_7"], url=f"tg://user?id={owner_id}", style="primary"),
            styled_button(text=_["S_B_4"], url=config.SUPPORT_CHAT, style="primary"),
        ],
        [
            styled_button(text=_["S_B_3"], callback_data="open_help", style="success"),
        ],
    ]
    return buttons

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
