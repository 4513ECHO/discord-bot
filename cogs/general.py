from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    @commands.commnad()
    async def ping(self, ctx):
        ping = round(bot.latency * 1000)
        await ctx.send(f"pong! Botのping値は{ping}msです")

    @commands.command()
    async def add(self, ctx, *n: int):
        await ctx.send(f"{sum(n)}です")

def setup(bot):
    bot.add_cog(General(bot))
