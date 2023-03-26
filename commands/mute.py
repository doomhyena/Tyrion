import nextcord
import asyncio
from nextcord.ext import commands
@commands.has_permissions(manage_roles=True)

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="mute <felhasználó> [indok: opcionális]")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: nextcord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = nextcord.utils.get(guild.roles, name="Némított")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Némított")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
                await asyncio.sleep(2)
        embed = nextcord.Embed(title="Némítás", description=f"{member.mention} sikeresen le lett némítva ", colour=nextcord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"Le lettél némítva a **{guild.name}** szerveren!\n Indok: **{reason}**")


def setup(bot):
    bot.add_cog(Mute(bot))