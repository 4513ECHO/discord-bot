import discord
from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX', '#')

COGS_LIST = [
    'cogs.general',
    'cogs.affirm',
    'cogs.calc',
    'dispander',
]

class Main(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=commands.when_mentioned_or(command_prefix),
                         case_insensitive=True,
                         activity=discord.Game(f"{PREFIX}help to Help"),
                         )

        for cog in COGS_LIST:
            self.load_extension(cog)

    async def on_ready(self):
        print("ready. " + self.user.name)

bot = Main(command_prefix=PREFIX)
bot.run(TOKEN)

