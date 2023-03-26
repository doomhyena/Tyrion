import nextcord
import datetime
from nextcord.ext import commands


class Softban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="softban [felhasználó] (indok)")
    async def softban(self, ctx, member, *, reason):
        if ctx.author.guild_permissions.ban_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod kitiltani!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply("A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.ban_members: await ctx.reply("A botnak nincs joga kitiltáshoz!", mention_author=False); return
            else:
                try:
                    embed = nextcord.Embed(description=f"Ki lettél tiltva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed.add_field(name="Általa", value=ctx.author, inline=False)
                    embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                    embed.set_author(name="Ki lettél tiltva!", icon_url=ctx.guild.icon_url)
                    embed.set_footer(text="Radon × Kitiltás", icon_url=self.bot.user.display_avatar)
                    await member.send(embed=embed)
                except: pass
                await ctx.guild.ban(user=member, reason=reason, delete_message_days=7)
                embed2 = nextcord.Embed(description=f"**{member.name}** ki lett tiltva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                embed2.add_field(name="Indok", value=f"`{reason}`")
                embed2.set_author(name="Sikeres kitiltás!", icon_url=ctx.author.avatar_url)
                embed2.set_footer(text=f"{ctx.author.name} × Kitiltás", icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed2)
        else:
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return
    

def setup(bot):
    bot.add_cog(Softban(bot))
