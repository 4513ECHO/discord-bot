from discord.ext import commands
import lark
import os
import random

with open(os.path.dirname(__file__) + "/../docs/dice.lark") as f:
    dice_parser = lark.Lark(f.read(), start="expr")

class DiceTransformer(lark.Transformer):
    def expr(self, tree): return tree[0]

    def term(self, tree): return tree[0]

    def item(self, tree): return tree[0]

    def add(self, tree): return tree[0] + tree[1]

    def sub(self, tree): return tree[0] - tree[1]

    def dice(self, tree):
        result = 0
        for _ in range(tree[0]):
            result += random.randint(1, tree[1])
        return result

    def barabara(self, tree):
        result = []
        for _ in range(tree[0]):
            result.append(random.randint(1, tree[1]))
        return result

    def number(self, tree): return int(tree[0])

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['d'])
    async def dice(self, ctx, expr):
        tree = dice_parser.parse(expr)
        result = DiceTransformer().transform(tree)
        await ctx.send(f"{ctx.author.mention} [{expr}] -> {result}")

def setup(bot):
    bot.add_cog(Dice(bot))

