# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

import os
import asyncio

CPU = os.cpu_count() or 1

def _env_value(key, default=None):
    return os.environ[key] if key in os.environ else default

# Adaptive concurrency: lightweight on 1-core VPS, scales gently on multi-core
MAX_CONCURRENT = int(_env_value("MAX_CONCURRENT", str(min(16, max(4, CPU * 2)))))

# 512 KB chunks — perfectly balanced for fast network without high memory allocation
CHUNK_SIZE = int(_env_value("CHUNK_SIZE", str(512 * 1024)))

# Tighter yt-dlp timeout: fail fast, move to next method
YTDLP_TIMEOUT = int(_env_value("YTDLP_TIMEOUT", "25"))

# Efficient metadata cache: 10 min TTL with 512 entries (saves RAM)
YOUTUBE_META_TTL = int(_env_value("YOUTUBE_META_TTL", "600"))
YOUTUBE_META_MAX = int(_env_value("YOUTUBE_META_MAX", "512"))

SEM = asyncio.Semaphore(MAX_CONCURRENT)

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
