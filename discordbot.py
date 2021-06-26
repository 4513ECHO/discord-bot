import discord
import os
import re

TOKEN = os.environ["TOKEN"]

PREFIX = "#"

HELP_MESSAGE = f"""
```Alice Liddellの使い方(暫定版)``` \n
**Prefix**
  {PREFIX}

**Commads**
  help: このメッセージを表示します。
  neko: 「にゃーん」と返します。
  その他: 「そうだね」と返します。特殊なパターンもあります。
"""

MESSAGES = {r"help": HELP_MESSAGE,
            r"neko": "にゃーん",
            r"(死|し)にたい.*": "いきててえらいよ",
            r"結婚し.*": "きもいよ",
            r"やったぜ": "よかったね"
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
