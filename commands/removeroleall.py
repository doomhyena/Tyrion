import nextcord
import datetime
import asyncio
from nextcord.ext import commands


class Removeroleall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="removeroleall [@rang]", aliases=["removeall"])
    async def removeroleall(self, ctx, role):
        if ctx.author.guild_permissions.manage_roles:
            role = await commands.RoleConverter().convert(ctx, role)
            await ctx.reply("Kérlek várj...")
            for member in ctx.guild.members:
                try: await member.remove_roles(role)
                except: continue
                await asyncio.sleep(1)
            await ctx.send(f"Sikeresen elvettem az összes felhasználótól a {role.name} rangot!")
        else:
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)    

def setup(bot):
    bot.add_cog(Removeroleall(bot))