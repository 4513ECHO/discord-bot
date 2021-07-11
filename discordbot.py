from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX', '#')

COGS_LIST = [
    'cogs.general',
    'cogs.affirm',
    'dispander',
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in COGS_LIST:
            self.load_extension(cog)

    async def on_ready(self):
        print("--Boot--")
        print("name: ", self.user.name)
        print("id: ", self.user.id)
        print("--------")

bot = MyBot(command_prefix=PREFIX)
bot.run(TOKEN)
