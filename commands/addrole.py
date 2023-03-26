import nextcord
import datetime
from nextcord.ext import commands


class Addrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="addrole [@említés] [@rang]")
    async def addrole(self, ctx, user, *, role):   
        if ctx.author.guild_permissions.manage_roles == False: 
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            try: user = await commands.MemberConverter().convert(ctx, user)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            try: role = await commands.RoleConverter().convert(ctx, role)
            except:
                embed = nextcord.Embed(description="Nem található ilyen rang a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed = embed, mention_author=False)
                return
            if ctx.author.id == user.id: 
                embed = nextcord.Embed(description="Nem adhatsz magadnak rangot!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            elif ctx.author.guild.owner == False:
                if ctx.author.top_role < role: 
                    embed = nextcord.Embed(description="Ez a rang magasabb mint a te rangod, ezért nem adhatod oda másnak!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            else:
                pass
            bot = await commands.MemberConverter().convert(ctx, str(713014602891264051))
            if bot.guild_permissions.manage_roles == False: 
                embed = nextcord.Embed(description="Nincs jogosultságom a felhasználó kezelésére!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            await user.add_roles(role)
            embed = nextcord.Embed(description=f":white_check_mark: {role.mention} sikeresen odaadva {user.mention} számára!", timestamp = datetime.datetime.utcnow(), color=0xff9900)
            embed.set_author(name="Rang adás", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{ctx.author} × Rang adás", icon_url=self.bot.user.display_avatar)
            await ctx.reply(embed=embed, mention_author=False)
def setup(bot):
    bot.add_cog(Addrole(bot))
