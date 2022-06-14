import random

import lark
from discord.ext import commands

from .. import settings

logger = settings.get_logger(__name__)
dice_parser = lark.Lark(settings.load_asset("dice.lark"), start="statement")


class DiceTransformer(lark.Transformer):
    def statement(self, tree):
        return tree[0]

    def expr(self, tree):
        return tree[0]

    def term(self, tree):
        return tree[0]

    def equal(self, tree):
        if tree[0] == tree[1]:
            return [tree[0][0], True]
        else:
            return [tree[0][0], False]

    def more(self, tree):
        if tree[0] >= tree[1]:
            return [tree[0][0], True]
        else:
            return [tree[0][0], False]

    def less(self, tree):
        if tree[0] <= tree[1]:
            return [tree[0][0], True]
        else:
            return [tree[0][0], False]

    def add(self, tree):
        return [tree[0][0] + tree[1][0]]

    def sub(self, tree):
        return [tree[0][0] - tree[1][0]]

    def dice(self, tree):
        result = 0
        for _ in range(tree[0][0]):
            result += random.randint(1, tree[1][0])
        return [result]

    def barabara(self, tree):
        result = []
        for _ in range(tree[0][0]):
            result.append(random.randint(1, tree[1][0]))
        return [result]

    def number(self, tree):
        return [int(tree[0])]


class Dice(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(aliases=[])
    async def dice(self, ctx, *, expr) -> None:
        logger.info("execute command 'dice'")
        try:
            tree = dice_parser.parse(expr)
            logger.debug("parse expression")
            result = DiceTransformer().transform(tree)
            logger.debug("transform expression")
        except Exception as e:
            await ctx.send("エラーが発生しました。正しい式ではありません")
            logger.warning("parse expression is failed")
            return
        if result[1:2]:
            if result[1]:
                result[1] = "Success"
            else:
                result[1] = "Failure"
            await ctx.send(
                f"{ctx.author.mention} [{expr}] -> {result[0]} ({result[1]})"
            )
        else:
            await ctx.send(f"{ctx.author.mention} [{expr}] -> {result[0]}")
        logger.debug("command 'dice' is successed")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Dice(bot))
    logger.debug("cog is loaded")
