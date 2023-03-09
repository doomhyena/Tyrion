import asyncio
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= discord.Intents.all())
@commands.has_permissions(manage_messages=True)

class RemoveTimeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def removetimeout(ctx, member: discord.Member, *, reason=None):
        timeout_role = discord.utils.get(ctx.guild.roles, name="Timeout")
        await member.remove_roles(timeout_role, reason=reason)
        await ctx.send(f"{member.mention} időkorlátozása eltávolítva. Ok: {reason}")

def setup(bot):
    bot.add_cog(RemoveTimeout(bot))