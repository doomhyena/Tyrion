import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= discord.Intents.all())
@commands.has_permissions(kick_members=True)

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason) 
        await ctx.send(f"{member.mention} ki lett rúgva. Ok: {reason}")

def setup(bot):
    bot.add_cog(Kick(bot))