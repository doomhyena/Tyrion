import nextcord
from nextcord.ext import commands


class Serverlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @bot.command()
        async def serverlist(ctx):
            if ctx.author.id == 864583234158460938 or ctx.author.id == 1056315640048263230 or ctx.author.id == 452133888047972352:
                for guild in bot.guilds:
                    print(f"{guild.name} ({len(guild.members)})")
                    await ctx.message.delete()

def setup(bot):
    bot.add_cog(Serverlist(bot))
