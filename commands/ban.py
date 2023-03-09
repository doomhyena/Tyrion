import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= discord.Intents.all())
@commands.has_permissions(ban_members=True)

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} sikeresen ki lett tiltva.')

def setup(bot):
    bot.add_cog(Ban(bot))