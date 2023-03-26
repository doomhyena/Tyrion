import nextcord
from nextcord.ext import commands


class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="unmute <felhasználó>")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: nextcord.Member):
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Némított")

        await member.remove_roles(mutedRole)
        await member.send(f"A némításod fel lett oldva a **{ctx.guild.name}** szerveren!")
        embed = nextcord.Embed(title="Némítás feloldása", description=f"Sikeresen feloldva {member.mention} a némítás alól",colour=nextcord.Colour.light_gray())
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Unmute(bot))
