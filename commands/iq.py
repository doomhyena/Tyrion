import nextcord
import random
import datetime
from nextcord.ext import commands


class Iq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(usage="iq (@felhasználó)")
    async def iq(self, ctx, member=None):
        if member == None:
            embed = nextcord.Embed(  title="IQ",
                                    description=f"{ctx.author.mention} IQ-ja: **{random.randint(60, 230)}** IQ pont. Büszkék vagyunk rád.",
                                    color=0xe9b703,
                                    timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Radon × IQ", icon_url=ctx.author.display_avatar)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            try:
                member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó! <:radon_x:811191514482212874>", color=0xFF9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Radon × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed)
                return
            embed = nextcord.Embed(title="IQ", description=f"{member.mention} IQ-ja: **{random.randint(60, 170)}** IQ pont. Büszkék vagyunk rád.", color=0xe9b703, timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
def setup(bot):
    bot.add_cog(Iq(bot))
