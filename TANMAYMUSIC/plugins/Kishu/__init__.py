# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

import glob
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
