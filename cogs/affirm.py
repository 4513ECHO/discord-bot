from discord.ext import commands
import os
import csv
import re

AFFIRM_ROLE = 860116340672036915

with open(os.path.dirname(__file__) + "/../docs/messages.csv") as f:
    messages = dict(filter(None, csv.reader(f)))

class Affirm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['af'])
    async def affirm(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("サブコマンドが指定されていません")

    @affirm.command(aliases=['add'])
    async def add_member(self, ctx):
        await ctx.author.add_roles(ctx.guild.get_role(AFFIRM_ROLE))
        await ctx.send(f"{ctx.author.mention} ロールを追加しました")

    @affirm.command(aliases=['rm'])
    async def remove_member(self, ctx):
        await ctx.author.remove_roles(ctx.guild.get_role(AFFIRM_ROLE))
        await ctx.send(f"{ctx.author.mention} ロールを削除しました")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not(message.guild.get_role(AFFIRM_ROLE) in message.author.roles):
            return

        for x in messages.keys():
            if re.match(x, message.content):
                await message.channel.send(messages[x])
                return
        await message.channel.send("そうだね")

def setup(bot):
    bot.add_cog(Affirm(bot))
