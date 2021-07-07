from discord.ext import commands
import os
import dotenv
import re

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

INITAL_EXTENSIONS = [
    'cogs.testcog'
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)


        for cog in INITAL_EXTENSIONS:
            self.load_extension(cog)

    async def on_ready(self):
        print("-----")
        print(self.user.name)
        print(self.user.id)
        print("-----")

bot = MyBot(command_prefix="#")
bot.run(TOKEN)
