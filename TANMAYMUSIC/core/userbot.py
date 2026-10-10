# ═══════════════════════════════════════════════════════════
#        🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   GɪᴛHᴜʙ : github.com/tanmayjn2015/tanmay-music-bot
#   Dᴇᴠʟᴏᴘᴇʀ : @tanmayjn2015 | Telegram
# ═══════════════════════════════════════════════════════════

from pyrogram import Client, errors

import config

from ..logging import LOGGER

assistants = []
assistantids = []

GROUPS_TO_JOIN = []  # Add public support groups here if needed.


# Initialize userbots
class Userbot:
    def __init__(self):
        self.one = Client(
            "TANMAYAssis1",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            in_memory=True,
            workers=2,
            sleep_threshold=60,
        )
        self.two = Client(
            "TANMAYAssis2",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
            in_memory=True,
            workers=2,
            sleep_threshold=60,
        )
        self.three = Client(
            "TANMAYAssis3",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
            in_memory=True,
            workers=2,
            sleep_threshold=60,
        )
        self.four = Client(
            "TANMAYAssis4",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
            in_memory=True,
            workers=2,
            sleep_threshold=60,
        )
        self.five = Client(
            "TANMAYAssis5",
            config.API_ID,
            config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
            in_memory=True,
            workers=2,
            sleep_threshold=60,
        )

    async def start_assistant(self, client: Client, index: int):
        string_attr = [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5,
        ][index - 1]
        if not string_attr:
            return

        while True:
            try:
                await client.start()
                break
            except errors.FloodWait as e:
                LOGGER(__name__).warning(f"⚠️ Assistant {index} FloodWait. Waiting {e.value}s...")
                await asyncio.sleep(e.value + 1)
            except Exception as e:
                LOGGER(__name__).error(f"❌ Failed to start Assistant {index}: {e}")
                return

        for group in GROUPS_TO_JOIN:
            try:
                await client.join_chat(group)
            except Exception:
                pass

        assistants.append(index)

        try:
            await client.send_message(
                config.LOGGER_ID, f"TANMAY Assistant {index} Started"
            )
        except Exception:
            LOGGER(__name__).warning(
                f"Assistant {index} cannot access the log group – continuing."
            )

        me = await client.get_me()
        client.id, client.name, client.username = me.id, me.first_name, me.username
        assistantids.append(me.id)

        LOGGER(__name__).info(f"Assistant {index} Started as {client.name}")

    async def start(self):
        LOGGER(__name__).info("Starting TANMAY Assistants...")
        await self.start_assistant(self.one, 1)
        await self.start_assistant(self.two, 2)
        await self.start_assistant(self.three, 3)
        await self.start_assistant(self.four, 4)
        await self.start_assistant(self.five, 5)

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error while stopping assistants: {e}")

# ═══════════════════════════════════════════════════════════
#         🌺 𝗧𝗔𝗡𝗠𝗔𝗬 𝗠𝗨𝗦𝗜𝗖 🌺
#   github.com/tanmayjn2015/tanmay-music-bot
# ═══════════════════════════════════════════════════════════
