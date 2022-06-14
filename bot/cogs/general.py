
import discord
import dispander
from discord.ext import commands

from .. import settings

with open(os.path.dirname(__file__) + "/otani_meigen.txt") as f:
    otani_meigen: list[str] = f.readlines()

auto_reactions_channels = settings.DB.auto_reactions_channels
fake_ban_server = settings.DB.fake_ban_server
expand_message_server = settings.DB.expand_message_server


class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
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
                "そのユーザーはすでにBANされています!\n(このメッセージは5秒後に削除されます)", delete_after=5
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
        await auto_reactions_channels.insert_one(
            {"channelid": channel.id, "emojis": emojis}
        )
        await ctx.send(f"{channel.name}の自動リアクションを開始しました")

    @commands.command()
    async def remove_auto_reactions(self, ctx, channel: discord.TextChannel):
        result = await auto_reactions_channels.delete_one({"channelid": channel.id})
        if result.deleted_count == 0:
            return await ctx.send(f"{channel.name}では自動リアクションを行なっていません")
        await ctx.send(f"{channel.name}の自動リアクションを停止しました")

    @commands.Cog.listener(name="on_message")
    async def auto_add_reactions(self, message):
        if message.author.bot:
            return
        channel = await auto_reactions_channels.find_one(
            {"channelid": message.channel.id}, {"_id": False}
        )
        if channel is None:
            return
        for emoji in channel["emojis"]:
            await message.add_reaction(emoji)
        # await message.channel.send(channel)

        await message.add_reaction(channel)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
    logger.debug("cog is loaded")
