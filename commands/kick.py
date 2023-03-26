import nextcord
import datetime
from nextcord.ext import commands
@commands.has_permissions(kick_members=True)

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage="kick [felhasználó] (indok)", aliases=["kirúg", "kirug", "kirugás", "kirúgás", "kirúgas"])
    async def kick(self, ctx, member, *, reason="Nincs indok megadva."):
        if ctx.author.guild_permissions.kick_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren! <:radon_x:811191514482212874>", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("<:radon_x:856423841667743804> Magadat nem tudod kirúgni!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply("<:radon_x:856423841667743804> A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("<:radon_x:856423841667743804> A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.kick_members: await ctx.reply("<:radon_x:856423841667743804> A botnak nincs joga kirúgáshoz!", mention_author=False); return
            else:
                try:
                    embed = nextcord.Embed(description=f"Ki lettél rúgva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed.add_field(name="Általa", value=ctx.author, inline=False)
                    embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                    embed.set_author(name="Ki lettél rúgva!", icon_url=ctx.author.display_avatar)
                    embed.set_footer(text="Rebus × Kirúgás", icon_url=self.client.user.display_avatar)
                    await member.send(embed=embed)
                except: pass
                await ctx.guild.kick(user=member, reason=reason)
                embed2 = nextcord.Embed(description=f"**{member.name}** ki lett rúgva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                embed2.add_field(name="Indok", value=f"`{reason}`")
                embed2.set_author(name="Sikeres kirúgás!", icon_url=ctx.author.display_avatar)
                embed2.set_footer(text=f"{ctx.author.name} x Kirúgás", icon_url=self.client.user.display_avatar)
                await ctx.send(embed=embed2)
        else:
            perm = "Tagok kirúgása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

def setup(bot):
    bot.add_cog(Kick(bot))