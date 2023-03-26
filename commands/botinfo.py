import nextcord
import platform
import datetime
import psutil
from nextcord.ext import commands


class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["botinfo", "bot-info", "binfo", "bi", "boti"])
    async def botinfó(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = nextcord.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))
        channelCount = len(set(self.client.get_all_channels()))
        embed = nextcord.Embed(description="A Radon bot információi", color=0xFF9900, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Bot neve", value="Radon", inline=True)
        embed.add_field(name="Készült", value="2021.02.03", inline=True)
        embed.add_field(name="Programozási könytár", value="Nextcord")
        embed.add_field(name="Szerverek", value=f"{serverCount}")
        embed.add_field(name="Csatornák", value=f"{channelCount}")
        embed.add_field(name="Felhasználók", value=f"{memberCount}")
        embed.add_field(name="Python verzió", value=f"{pythonVersion}")
        embed.add_field(name="Parancsok száma", value=f"{len(self.client.commands)}")
        embed.add_field(name="Nextcord verzió", value=f"{dpyVersion}")
        embed.add_field(name="Operációs rendszer", value=f"Debian 10")
        embed.add_field(name="CPU kihasználtság", value=f"{psutil.cpu_percent()}%")
        embed.add_field(name="Memória kihasználtság", value=f"{psutil.virtual_memory().percent}%")
        embed.set_author(name="Bot információi", icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"{ctx.author.name} × Bot infók", icon_url=self.client.user.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Botinfo(bot))
