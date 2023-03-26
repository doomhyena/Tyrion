import nextcord
import random
from nextcord.ext import commands


class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["dobokocka", "baszdfejbemagadat"])
    async def dice(self, ctx):
        await ctx.send(f"🎲 {random.randint(1, 6)}")
    

def setup(bot):
    bot.add_cog(Dice(bot))
