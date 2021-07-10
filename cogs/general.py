from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    @commands.command()
    async def add(self, ctx, *n: int):
        await ctx.send(f"{sum(n)}です")

def setup(bot):
    bot.add_cog(General(bot))
