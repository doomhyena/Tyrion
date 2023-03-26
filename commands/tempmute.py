import nextcord
import asyncio
import convert
import datetime
from nextcord.ext import commands


class Tempmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="tempmute [felhasználó] [idő] (indok)")
    async def tempmute(self, ctx, member, ido, *, reason="Nincs indok megadva"):
        if ctx.author.guild_permissions.kick_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.client.user.avatar_url)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.avatar_url)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod lenémítani!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply(" A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.manage_roles: await ctx.reply("A botnak nincs joga rangok adásához!", mention_author=False); return
            else:
                embed = nextcord.Embed(description=f"{member.mention} le lett némítva {ctx.author.mention} által!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name="Némítás", icon_url=ctx.author.display_avatar)
                embed.add_field(name="Indok", value=f"`{reason}`")
                embed.add_field(name="Időtartam", value=ido)
                embed.set_footer(text=f"{ctx.author.name} × Némítás", icon_url=self.bot.user.display_avatar)
                if not nextcord.utils.get(ctx.guild.roles, name="Némított"):
                    msg = await ctx.reply("Kérlek várj, amíg létrehozom a rangot és bekonfigurálom a rendszert...", mention_author=False)
                    mutedrole = await ctx.guild.create_role(name="Némított", colour=0xff9900, reason=f"Némítás - {ctx.author.name} - Egyszeri alkalom")
                    overwrites = {
                        mutedrole: nextcord.PermissionOverwrite(send_messages=False)
                    }
                    for i in ctx.guild.channels: await i.edit(overwrites=overwrites)
                    await msg.delete()
                try: ido=convert(ido)
                except: await ctx.reply("<:radon_x:856423841667743804> Helytelen időformátum!", mention_author=False); return
                await member.add_roles(nextcord.utils.get(ctx.guild.roles, name="Némított"))
                await ctx.reply(embed=embed, mention_author=False)
                await asyncio.sleep(ido)
                await member.remove_roles(nextcord.utils.get(ctx.guild.roles, name="Némított"))
        else:
            perm = "Tagok kirúgása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

def setup(bot):
    bot.add_cog(Tempmute(bot))
