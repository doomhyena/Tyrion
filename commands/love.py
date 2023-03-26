import nextcord
import asyncio
import datetime
import random
from nextcord.ext import commands


class Love(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @commands.command(usage="love [1. felhasználó] [2. felhasználó]")
        async def love(self, ctx, member1, member2):
            try: member1 = await commands.MemberConverter().convert(ctx, member1); member2 = await commands.MemberConverter().convert(ctx, member2)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó!", color=0xFF9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Tyrion × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed)
                return
            if member1 == member2: await ctx.reply("Aww, nyilván 100%, szeresd magad :)", mention_author=False);return
            embed = nextcord.Embed(description=f"{member1.mention} :grey_question: {member2.mention} [SZÁMOLÁS...]", color=0xe9b603, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Szeretet", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{member1.name} - {member2.name} × Kérte: {ctx.author.name}", icon_url=self.client.user.display_avatar)
            msg = await ctx.reply(embed=embed, mention_author=False)
            szam = random.randint(0, 100)
            if szam >= 90: emoji=":heart_on_fire:"
            if szam >=70 and szam< 90: emoji=":revolving_hearts:"
            if szam >=50 and szam<70: emoji=":heart:"
            if szam >=30 and szam<50: emoji=":broken_heart:"
            if szam >=0 and szam<30: emoji=":mending_heart:"
            await asyncio.sleep(random.randint(1, 4))
            embed = nextcord.Embed(description=f"{member1.mention} {emoji} {member2.mention} [**{szam}%**]")
            embed.set_author(name="Szeretet", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{member1.name} - {member2.name} × Kérte: {ctx.author.name}", icon_url=self.client.user.display_avatar)
            await msg.edit(embed=embed, content=None)

def setup(bot):
    bot.add_cog(Love(bot))
