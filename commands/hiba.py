import nextcord
import datetime
from nextcord.ext import commands


class Hiba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.cooldown(1, 300, type=commands.BucketType.user)
    async def hiba(self, ctx, *, uzenet):
        embed = nextcord.Embed(title=f"{ctx.author} hibát jelentett", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="Hiba", value=uzenet)
        channel = self.client.get_channel(806906693191073862)
        await channel.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Hiba(bot))
