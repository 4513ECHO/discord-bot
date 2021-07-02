from discord.ext import commands
import os
import re
import traceback

TOKEN = os.environ["TOKEN"]

INITAL_EXTENSIONS = [
    'cogs.testcog'
]

PREFIX = "#"

MESSAGES = {r"neko": "にゃーん",
            r"(死|し)にたい": "いきててえらいよ",
            r"やったぜ": "よかったね",
            r"かわいい.*\?$": "もちろんそうだよ",
            r"かわいい": "ありがとう",
            r"病んだ": "げんきあげる",
            r"ありがとう": "こちらこそ",
            r"(かなしい|悲しい|つらい|辛い|)": "はなしきくよ",
            r"(つかれた|疲れた)": "ゆっくり休んで いきててえらいね",
            r"^ねえねえ": "なあに",
            r"こんにちは": "こんにちは",
            r"おはよう": "おはよう",
            r"おやすみ": "おやすみ"
           }

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        for cog in INITAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print("-----")
        print(self.user.name)
        print(self.user.id)
        print("-----")


@client.event
async def on_message(message):
    msg = message.content
    if message.author.bot or not msg.startswith(PREFIX):
        return

    for x in MESSAGES.keys():
        if re.match(x, msg.strip(PREFIX)):
            await message.channel.send(MESSAGES[x])
            return
    await message.channel.send("そうだね")

if __name__ == '__main__':
    bot = MyBot(command_prefix=PREFIX)
    bot.run(TOKEN)

