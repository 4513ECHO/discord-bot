import discord
from discord.ext import commands

import settings

COGS_LIST = [
    "cogs.general",
    "cogs.affirm",
    "cogs.calc",
    "cogs.dice",
]


class Main(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.typing = False
        intents.members = True
        super().__init__(
            command_prefix=commands.when_mentioned_or(command_prefix),
            intents=intents,
            case_insensitive=True,
            activity=discord.Game(f"{settings.PREFIX}help to Help"),
        )

        for cog in COGS_LIST:
            self.load_extension(cog)

    async def on_ready(self):
        appinfo = await self.application_info()
        self.owner_id = appinfo.owner.id
        print(f"ready. {self.user.name}(id: {self.user.id})")


bot = Main(command_prefix=settings.PREFIX)
bot.run(settings.TOKEN)
