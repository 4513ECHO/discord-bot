import discord
from discord.ext import commands
import dispander


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dispand_flag = True
        self.fake_banned_flag = True
        self.auto_reactions_channels = dict()

    @commands.command()
    async def neko(self, ctx):
        await ctx.send("にゃーん")

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f"pong! Botのping値は{ping}msです")

    @commands.Cog.listener(name="on_message")
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

    @commands.Cog.listener(name="on_message")
    async def fake_banned(self, message):
        if message.author.bot:
            return
        if not self.fake_banned_flag:
            return

        if self.bot.get_user(self.bot.owner_id).mention in message.content:
            await message.channel.send(
                "そのユーザーはすでにBANされています!\n(このメッセージは5秒後に削除されます)",
                delete_after=5
            )

    @commands.command()
    async def fake_ban(self, ctx, on_flag: bool):
        if on_flag:
            self.fake_banned_flag = True
            await ctx.send("偽BAN状態をオンにしました")
        else:
            self.fake_banned_flag = False
            await ctx.send("偽BAN状態をオフにしました")

    @commands.command()
    async def auto_reactions(self, ctx, channel: discord.TextChannel, *emojis: str):
        self.auto_reactions_channels[channel.id] = emojis
        await ctx.send(f"{channel.name}の自動リアクションを開始しました")

    @commands.command()
    async def remove_auto_reactions(self, ctx, channel: discord.TextChannel):
        ch = self.auto_reactions_channels.pop(channel.id, None)
        if ch is None:
            await ctx.send(f"{channel.name}では自動リアクションを行なっていません")
            return
        await ctx.send(f"{channel.name}の自動リアクションを停止しました")

    @commands.Cog.listener(name="on_message")
    async def auto_add_reactions(self, message):
        if message.author.bot:
            return
        if message.channel.id not in self.auto_reactions_channels:
            return

        for x in self.auto_reactions_channels[message.channel.id]:
            await message.add_reaction(x)


def setup(bot):
    bot.add_cog(General(bot))
