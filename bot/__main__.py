import asyncio

import discord
from discord.ext import commands

from . import settings

COGS_LIST = [
    "bot.cogs.general",
    "bot.cogs.affirm",
    "bot.cogs.calc",
    "bot.cogs.dice",
    "bot.cogs.mongodb_testing",
    "jishaku",
]

discord_logger = settings.get_logger("discord")
logger = settings.get_logger(__name__)


class MainBot(commands.Bot):
    def __init__(self, command_prefix: str) -> None:
        intents = discord.Intents.default()
        intents.typing = False
        intents.members = True
        allowed_mentions = discord.AllowedMentions(replied_user=False)
        super().__init__(
            command_prefix=commands.when_mentioned_or(command_prefix),
            intents=intents,
            case_insensitive=True,
            allowed_mentions=allowed_mentions,
            activity=discord.Game(f"help command: {settings.PREFIX}help"),
        )

    async def on_ready(self) -> None:
        appinfo = await self.application_info()
        self.owner_id = appinfo.owner.id
        logger.info(f"{self.user.name} is ready. (id: {self.user.id})")


async def run() -> None:
    bot = MainBot(command_prefix=settings.PREFIX)
    for cog in COGS_LIST:
        await bot.load_extension(cog)
        logger.debug(f"cog {cog} is loaded")
    await bot.start(token=settings.TOKEN)


def main() -> None:
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        logger.warn("interrupted")
        return


if __name__ == "__main__":
    main()
