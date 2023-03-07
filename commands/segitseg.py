import discord
import datetime
from discord.ext import commands

class Segitsegcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def segitseg(self, ctx):
        embed = discord.Embed(title="Ez a segítség menü. tt találod meg a parancsaimat!", description = "Minden parancs elé tegyél !-et hogy működjön a parancs!", color = 0xff0000)

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(icon_url=ctx.author.avatar_url, name=f'{ctx.author}')
        embed.add_field(name="!segitseg", value="Ez a menü rendszer Itt a találod a parancsaimat!", inline=False)
        embed.set_footer(icon_url=ctx.guild.icon_url, text=ctx.guild.name)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Segitsegcommand(bot))