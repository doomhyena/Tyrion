import discord
import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= discord.Intents.all())

class Segitsegcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def segitseg(self, ctx):
        embed = discord.Embed(title="Ez a segítség menü. tt találod meg a parancsaimat!", description = "Minden parancs elé tegyél **t!**-et hogy működjön a parancs!", color = 0xff0000)

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(icon_url=ctx.author.avatar_url, name=f'{ctx.author}')
        embed.add_field(name="t!ban", value="Ezzel a paranccsal tudod kitiltani az adott felhasználót `t!ban <@user> [indok]", inline=False)
        embed.add_field(name="t!mute", value="Ezzel a paranccsal tudod lenémítani az adott felhasználót `t!mute <@user> [indok]", inline=False)
        embed.add_field(name="t!segitseg", value="Ez a menü rendszer Itt a találod a parancsaimat!", inline=False)
        embed.set_footer(icon_url=ctx.guild.icon_url, text=ctx.guild.name)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Segitsegcommand(bot))