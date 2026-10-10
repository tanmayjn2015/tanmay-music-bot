# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

import logging
from logging.handlers import RotatingFileHandler

LOG_FILE = "log.txt"
LOG_LEVEL = "INFO"

FORMAT = "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
DATEFMT = "%d-%b-%y %H:%M:%S"

logging.basicConfig(
    level=LOG_LEVEL,
    format=FORMAT,
    datefmt=DATEFMT,
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(LOG_FILE, maxBytes=10_000_000, backupCount=3, encoding="utf-8"),
    ],
)

for lib, level in [
    ("httpx", logging.ERROR),
    ("pyrogram", logging.ERROR),
    ("pytgcalls", logging.ERROR),
    ("pymongo", logging.ERROR),
    ("ntgcalls", logging.CRITICAL),
]:
    logging.getLogger(lib).setLevel(level)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
