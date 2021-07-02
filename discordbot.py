import discord
import os
import re

TOKEN = os.environ["TOKEN"]

PREFIX = "#"

MESSAGES = {r"neko": "にゃーん",
            r"(死|し)にたい": "いきててえらいよ",
            r"やったぜ": "よかったね",
            r"かわいい.*\?$": "もちろんそうだよ",
            r"かわいい": "ありがとう",
            r"病んだ": "げんきあげる",
            r"ありがとう": "こちらこそ",
            r"(かなしい|悲しい|つらい|辛い)": "はなしきくよ",
            r"(つかれた|疲れた)": "ゆっくり休んで いきててえらいね",
            r"^ねえねえ": "なあに",
            r"こんにちは": "こんにちは",
            r"おはよう": "おはよう",
            r"おやすみ": "おやすみ"
           }

client = discord.Client()

@client.event
async def on_ready():
    print("起動しました")

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

client.run(TOKEN)
