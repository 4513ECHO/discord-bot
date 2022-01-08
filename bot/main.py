import logging

import discord
import settings
from discord.ext import commands

COGS_LIST = [
    "cogs.general",
    "cogs.affirm",
    "cogs.calc",
    "cogs.dice",
    "jishaku",
]

# TODO: rename docs/ to assets/

class Main(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.typing = False
        intents.members = True
        allowed_mentions = discord.AllowedMentions(replied_user=False)
        super().__init__(
            command_prefix=commands.when_mentioned_or(command_prefix),
            intents=intents,
            case_insensitive=True,
            allowed_mentions=allowed_mentions,
            activity=discord.Game(f"{settings.PREFIX}help to Help"),
        )

        for cog in COGS_LIST:
            self.load_extension(cog)

    async def on_ready(self):
        appinfo = await self.application_info()
        self.owner_id = appinfo.owner.id
        print(f"ready. {self.user.name}(id: {self.user.id})")


# TODO: streamhandler
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

bot = Main(command_prefix=settings.PREFIX)
print(f"TOKEN: {settings.TOKEN}")
bot.run(settings.TOKEN)
