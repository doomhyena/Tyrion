import nextcord
import asyncio
import datetime
from nextcord.ext import commands


class Unbanall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unbanall(self, ctx):
        if ctx.author.guild_permissions.ban_members:
            msg = await ctx.reply(content="Kérlek, várj...", mention_author=False)
            for member in await ctx.guild.bans():
                await ctx.guild.unban(member.user)
                await asyncio.sleep(2)
            await msg.edit("Sikeresen feloldottam az összes felhasználót!")
        else:
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return
    

def setup(bot):
    bot.add_cog(Unbanall(bot))
