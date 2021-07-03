from discord.ext import commands
import re

messages = {}
with open("messages.txt", 'r') as f:
    for x in f:
        l = x.split()
        messages[l[0]] = l[1]

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    @commands.command()
    async def add(self, ctx, n: int, m: int):
        await ctx.send(f"{n+m}です")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        for x in MESSAGES.keys():
            if re.match(x, message.content):
                await message.channel.send(MESSAGES[x])
                return
        await message.channel.send("そうだね")

def setup(bot):
    bot.add_cog(TestCog(bot))
