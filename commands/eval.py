import nextcord
import inspect
from nextcord.ext import commands


class Eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @bot.command(usage=["eval [parancs]"])
        async def eval(ctx, *, command):
            if ctx.message.author.id == 864583234158460938 or 1056315640048263230 or 452133888047972352:
                res = eval(command)
                if inspect.isawaitable(res):
                    await ctx.send(await res)
            else:
             await ctx.send(res)
    

def setup(bot):
    bot.add_cog(Eval(bot))
