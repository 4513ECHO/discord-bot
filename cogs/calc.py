from discord.ext import commands
import lark
import os

with open(os.path.dirname(__file__) + "/../docs/calc.lark") as f:
    parser = lark.Lark(f.read(), start="statement")

class CalcTransformer(lark.Transformer):
    def statement(self, tree): return tree[0]

    def expr(self, tree): return tree[0]

    def term(self, tree): return tree[0]

    def item(self, tree): return tree[0]

    def neg(self, tree): return - tree[0]

    def pow(self, tree): return tree[0] ** tree[1]

    def add(self, tree): return tree[0] + tree[1]

    def sub(self, tree): return tree[0] - tree[1]

    def mul(self, tree): return tree[0] * tree[1]

    def div(self, tree): return tree[0] / tree[1]

    def number(self, tree):
        if str(tree[0]).endswith(".0"):
            return int(tree[0])
        return float(tree[0])

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def solve(self, expr):
        tree = parser.parse(expr)
        result = CalcTransformer().transform(tree)
        return result

    @commands.command()
    async def calc(self, ctx, expr):
        try:
            result = self.solve(expr)
            await ctx.send(result)
        except Exception as e:
            await ctx.send("エラーが発生しました。正しい式ではありません")
            print(e)

    @commands.command()
    async def calq(self, ctx, expr):
        answer = self.solve(expr)
        await ctx.send(f"{expr}=?")

def setup(bot):
    bot.add_cog(Calc(bot))

