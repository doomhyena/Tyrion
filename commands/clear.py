import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= nextcord.Intents.all())
@commands.has_permissions(manage_messages=True)

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} üzenet törölve.")

def setup(bot):
    bot.add_cog(Clear(bot))