import nextcord
import convert
import datetime
import asyncio
from nextcord.ext import commands


class Tempban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @commands.command(usage="tempban [felhasználó] [idő] (indok)")
        async def tempban(self, ctx, member, ido, *, reason):
            if ctx.author.guild_permissions.ban_members:
                try: ido=convert(ido)
                except: await ctx.reply("<:radon_x:856423841667743804> Helytelen időformátum!", mention_author=False); return
                try: member = await commands.MemberConverter().convert(ctx, member)
                except: 
                    embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren! <:radon_x:811191514482212874>", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                    embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed1, mention_author=False)
                    return
                bot = await ctx.guild.fetch_member(1082312968525582467)
                if member.id == ctx.author.id: await ctx.reply("<:radon_x:856423841667743804> Magadat nem tudod kitiltani!", mention_author=False); return
                if member.top_role >= ctx.author.top_role: await ctx.reply("<:radon_x:856423841667743804> A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
                if bot.top_role < member.top_role: await ctx.reply("<:radon_x:856423841667743804> A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
                if not bot.guild_permissions.ban_members: await ctx.reply("<:radon_x:856423841667743804> A botnak nincs joga kitiltáshoz!", mention_author=False); return
                else:
                    try:
                        embed = nextcord.Embed(description=f"Ki lettél tiltva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                        embed.add_field(name="Általa", value=ctx.author, inline=False)
                        embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                        embed.set_author(name="Ki lettél tiltva!", icon_url=ctx.guild.icon_url)
                        embed.set_footer(text="Radon × Kitiltás", icon_url=self.bot.user.display_avatar)
                        await member.send(embed=embed)
                    except: pass
                    await ctx.guild.ban(user=member, reason=reason, delete_message_days=0)
                    embed2 = nextcord.Embed(description=f"**{member.name}** ki lett tiltva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed2.add_field(name="Indok", value=f"`{reason}`")
                    embed2.set_author(name="Sikeres kitiltás!", icon_url=ctx.author.display_avatar)
                    embed2.set_footer(text=f"{ctx.author.name} × Kitiltás", icon_url=self.bot.user.display_avatar)
                    await ctx.send(embed=embed2)
                    await asyncio.sleep(ido)
                    await ctx.guild.unban(member)
            else:
                perm = "Tagok kitiltása"
                embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
                await ctx.reply(embed=embed, mention_author=False)
                return

def setup(bot):
    bot.add_cog(Tempban(bot))
