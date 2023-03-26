import nextcord
import datetime
from nextcord.ext import commands


class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="unban [felhasználónév és tag, pl. Radon#6074", aliases=["ub", "felold", "kitiltasfelold", "kitiltásfelold", "feloldás"])
    async def unban(self, ctx, user):
        if ctx.author.guild_permissions.ban_members == False: 
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            if user.isdigit() == False: 
                lista = user.split('#')
                if len(lista) != 2: 
                    embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján! <:radon_x:811191514482212874>", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else: 
                    member_name = lista[0]
                    member_discriminator = lista[1]
                    banned_users = await ctx.guild.bans()
                    asd = False
                    for ban in banned_users:
                        if (ban.user.name, ban.user.discriminator) == (member_name, member_discriminator):
                            await ctx.guild.unban(ban.user)
                            embed = nextcord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xff9900, description = f"`{ban.user.name}#{ban.user.discriminator}` kitiltása `{ctx.author.name}#{ctx.author.discriminator}` által feloldásra került!")
                            embed.set_author(name="Kitiltás feloldása", icon_url=ctx.author.display_avatar)
                            embed.set_footer(text=f"{ctx.author} × Kitiltás feloldása", icon_url=self.client.user.display_avatarl)
                            await ctx.reply(embed=embed, mention_author=False)
                            asd = True
                            await user.send(f"A kitiltásod feloldották a **{ctx.author.guild_name}** szerveren!")
                    if asd == False:                         
                        embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján! <:radon_x:811191514482212874>", color=0xff9900, timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                        await ctx.reply(embed=embed, mention_author=False)
                        return
            else:
                banned_users = await ctx.guild.bans()
                lista = [b.user.id for b in banned_users]
                if int(user) not in lista: 
                    embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján! <:radon_x:811191514482212874>", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else:
                    user = await self.bot.fetch_user(user)
                    await ctx.guild.unban(user)
                    embed = nextcord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xff9900, description = f"`{user.name}#{user.discriminator}` kitiltása `{ctx.author.name}#{ctx.author.discriminator}` által feloldásra került!")
                    embed.set_author(name="Kitiltás feloldása", icon_url=ctx.author.display_avatar)
                    embed.set_footer(text=f"{ctx.author} × Kitiltás feloldása", icon_url=self.bot.user.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
    

def setup(bot):
    bot.add_cog(Unban(bot))
