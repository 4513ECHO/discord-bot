from discord.ext import commands
import re

MESSAGES = {}
with open("messages.txt", 'r') as f:
    for x in f:
        MESSAGES[x.split()[0]] = x.split()[1]

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

#    @commands.Cog.listener()
#    async def on_message(self, message):
#        msg = message.content
#        if message.author.bot:
#            return
#
#        for x in MESSAGES.keys():
#            if re.match(x, msg):
#                await message.channel.send(MESSAGES[x])
#                return
#        await message.channel.send("そうだね")

def setup(bot):
    bot.add_cog(TestCog(bot))
