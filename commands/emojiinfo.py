import nextcord
import datetime
from nextcord.ext import commands


class Emojiinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ei", "einfo", "emojii", "emoteinfo"], usage=",emojiinfo [emoji (alap discordos emojit a bot nem fogad el)]")
    async def emojiinfo(self, ctx, emoji: nextcord.Emoji):
        try: emoji = await emoji.guild.fetch_emoji(emoji.id)
        except nextcord.NotFound: return await ctx.reply("Nem találtam ilyen emojit.", mention_author=False)
        is_managed = "Igen" if emoji.managed else "Nem"
        is_animated = "Igen" if emoji.animated else "Nem"
        embed=nextcord.Embed(color=0xFF9900, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Név", value=f"`{emoji.name}`")
        embed.add_field(name="ID", value=f"{emoji.id}")
        embed.add_field(name="Letöltés", value=f"**[Kattints ide!]({emoji.url})**")
        embed.add_field(name="Dátum", value=f"{emoji.created_at.strftime('%Y. %m. %d. @ %H:%M:%S')}")
        embed.add_field(name="Feltöltötte", value=f"{emoji.user.mention} (**{emoji.user}**)")
        embed.add_field(name="Formátum", value=f"`<:{emoji.name}:{emoji.id}>`")
        embed.add_field(name="Animált?", value=f"{is_animated}")
        embed.add_field(name="Kezelt?", value=f"{is_managed}")
        embed.set_author(name="Emojiinfo", icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"{ctx.author.name} × Emojiinfo", icon_url=self.bot.user.display_avatar)
        embed.set_thumbnail(url=emoji.url)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await self.bot.process_commands(after)

def setup(bot):
    bot.add_cog(Emojiinfo(bot))
