from discord.ext import commands
import dispander
import asyncio

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dispand_flag = True
        self.fake_banned_flag = True

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

    @commands.Cog.listener(name='on_message')
    async def fake_banned(self, message):
        if message.author.bot:
            return
        if not self.fake_banned_flag:
            return

        if self.bot.get_user(self.bot.owner_id).mention in message.content:
            self_msg = await message.channel.send("そのユーザーはすでにBANされています!\n(このメッセージは5秒後に削除されます)")
            await asyncio.sleep(3)
            await self_msg.delete()

    @commands.command()
    async def fake_ban(self, ctx, on_flag: bool):
        if on_flag:
            self.fake_banned_flag = True
            await ctx.send("偽BAN状態をオンにしました")
        else:
            self.fake_banned_flag = False
            await ctx.send("偽BAN状態をオフにしました")

def setup(bot):
    bot.add_cog(General(bot))
