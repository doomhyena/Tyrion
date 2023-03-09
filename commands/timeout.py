import asyncio
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= discord.Intents.all())
@commands.has_permissions(manage_messages=True)

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def timeout(ctx, member: discord.Member, duration: int, *, reason=None):
        timeout_role = discord.utils.get(ctx.guild.roles, name="Timeout")
        await member.add_roles(timeout_role, reason=reason)
        await ctx.send(f"{member.mention} időkorlátozva lett {duration} másodpercre. Ok: {reason}")
        await asyncio.sleep(duration)
        await member.remove_roles(timeout_role, reason="Timeout vége")

def setup(bot):
    bot.add_cog(Timeout(bot))