from discord.ext import commands
import dispander

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dispand_flag = True

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"pong! Botのping値は{ping}msです")

    @commands.Cog.listener(name='on_message')
    async def do_dispand(self, message):
        if message.author.bot:
            return
        if self.dispand_flag:
            await dispander.dispand(message)

    @commands.command()
    async def expand_message(self, ctx, on_flag: bool):
        if on_flag:
            self.dispand_flag = True
            await ctx.send("メッセージ展開をオンにしました")
        else:
            self.dispand_flag = False
            await ctx.send("メッセージ展開をオフにしました")

def setup(bot):
    bot.add_cog(General(bot))
