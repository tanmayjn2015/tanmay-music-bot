# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

from TANMAYMUSIC.core.mongo import mongodb

coupledb = mongodb["couple"]

async def _doc(cid: int) -> dict:
    return await coupledb.find_one({"chat_id": cid}) or {}

async def get_couple(cid: int, date: str):
    doc = await _doc(cid)
    couple_map = doc.get("couple", {})

    if date not in couple_map:
        return None

    img_field = doc.get("img", {})
    img_path = img_field.get(date) if isinstance(img_field, dict) else img_field

    return {
        "user1": couple_map[date]["user1"],
        "user2": couple_map[date]["user2"],
        "img": img_path,
    }

async def save_couple(cid: int, date: str, couple: dict, img_path: str):
    doc = await _doc(cid)
    couple_map = doc.get("couple", {})
    img_field = doc.get("img", {})

    if not isinstance(img_field, dict):
        img_field = {}

    couple_map[date] = couple
    img_field[date] = img_path

    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": couple_map, "img": img_field}},
        upsert=True,
    )

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
