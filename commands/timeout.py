import asyncio
import nextcord
from nextcord.ext import commands
@commands.has_permissions(manage_messages=True)

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def timeout(ctx, member: nextcord.Member, duration: int, *, reason=None):
        timeout_role = nextcord.utils.get(ctx.guild.roles, name="Timeout")
        await member.add_roles(timeout_role, reason=reason)
        await ctx.send(f"{member.mention} időkorlátozva lett {duration} másodpercre. Ok: {reason}")
        await asyncio.sleep(duration)
        await member.remove_roles(timeout_role, reason="Timeout vége")

def setup(bot):
    bot.add_cog(Timeout(bot))