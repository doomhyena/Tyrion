import nextcord
import asyncio
import datetime
from nextcord.ext import commands


class Roleall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="roleall [@rang]")
    async def roleall(self, ctx, role):
        if ctx.author.guild_permissions.manage_roles:
            role = await commands.RoleConverter().convert(ctx, role)
            await ctx.reply("Kérlek várj...")
            for member in ctx.guild.members:
                try: await member.add_roles(role)
                except: continue
                await asyncio.sleep(1)
            await ctx.send(f"Sikeresen megkapta az összes felhasználó a {role.name} rangot!")
        else:
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Roleall(bot))
