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

    @commands.command(aliases=['af'])
    async def affirm(self, ctx, on_flag: bool):
        if on_flag:
            if ctx.guild.get_role(AFFIRM_ROLE) in ctx.author.roles:
                await ctx.send("すでにロールが追加されています")
                return
            await ctx.author.add_roles(ctx.guild.get_role(AFFIRM_ROLE))
            await ctx.send(f"{ctx.author.mention} ロールを追加しました")
        else:
            if not ctx.guild.get_role(AFFIRM_ROLE) in ctx.author.roles:
                await ctx.send("すでにロールが削除されています")
                return
            await ctx.author.remove_roles(ctx.guild.get_role(AFFIRM_ROLE))
            await ctx.send(f"{ctx.author.mention} ロールを削除しました")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.guild.get_role(AFFIRM_ROLE) in message.author.roles :
            return

        if message.content.startswith(tuple(await self.bot.get_prefix(message))):
            return

        for x in messages.keys():
            if re.match(x, message.content):
                await message.channel.send(messages[x])
                return
        await message.channel.send("そうだね")

def setup(bot):
    bot.add_cog(Affirm(bot))

