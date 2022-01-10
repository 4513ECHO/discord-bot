import discord
from discord.ext import commands

from cogs import settings

COGS_LIST = [
    "cogs.general",
    "cogs.affirm",
    "cogs.calc",
    "cogs.dice",
    "jishaku",
]

# TODO: rename docs/ to assets/
discord_logger = settings.get_logger("discord")
logger = settings.get_logger(__name__)


class Main(commands.Bot):
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

        for cog in COGS_LIST:
            self.load_extension(cog)
            logger.debug("cog {cog} is loaded")

    async def on_ready(self) -> None:
        appinfo = await self.application_info()
        self.owner_id = appinfo.owner.id
        logger.info(f"{self.user.name} is ready. (id: {self.user.id})")


bot = Main(command_prefix=settings.PREFIX)
logger.info(f"TOKEN: {settings.TOKEN}")
bot.run(settings.TOKEN)
