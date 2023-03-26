import nextcord
from nextcord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        commands.command()
        async def ping(ctx):
            await ctx.send(f"Pong! 🏓  {self.bot.latency * 1000:.0f}ms")

def setup(bot):
    bot.add_cog(Ping(bot))