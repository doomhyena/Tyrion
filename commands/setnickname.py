import nextcord
from nextcord.ext import commands


class Setnickname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["nick", "setnick"])
    async def setnickname(self, ctx, member: nextcord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Siekresen megváltoztattam {member.mention} felhasználónak a nevét!')
    

def setup(bot):
    bot.add_cog(Setnickname(bot))
