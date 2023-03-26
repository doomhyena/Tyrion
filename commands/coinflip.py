import nextcord
from nextcord.ext import commands
import random

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def coinflip(ctx, amount=5):
        num = random.randint(1, 2)
        if num == 1:
            await ctx.send("Fej!")
        if num == 2:
            await ctx.send("Írás!")

def setup(bot):
    bot.add_cog(Coinflip(bot))