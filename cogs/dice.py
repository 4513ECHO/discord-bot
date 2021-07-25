from discord.ext import commands
import lark
import os
import random

with open(os.path.dirname(__file__) + "/../docs/dice.lark") as f:
    dice_parser = lark.Lark(f.read(), start="statement")

class DiceTransformer(lark.Transformer):
    def statement(self, tree): return tree[0]

    def expr(self, tree): return tree[0]

    def term(self, tree): return tree[0]

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

    def add(self, tree): return [tree[0][0] + tree[1][0]]

    def sub(self, tree): return [tree[0][0] - tree[1][0]]

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

    def number(self, tree): return [int(tree[0])]

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['d'])
    async def dice(self, ctx, expr):
        try:
            tree = dice_parser.parse(expr)
            result = DiceTransformer().transform(tree)
        except Exception as e:
            await ctx.send("エラーが発生しました。正しい式ではありません")
            print(e)
            return
        if result[1:2]:
            if result[1]:
                result[1] = "Success"
            else:
                 result[1] = "Failure"
            await ctx.send(f"{ctx.author.mention} [{expr}] -> {result[0]} ({result[1]})")
        else:
            await ctx.send(f"{ctx.author.mention} [{expr}] -> {result[0]}")

def setup(bot):
    bot.add_cog(Dice(bot))

