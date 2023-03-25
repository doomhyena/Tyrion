import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= nextcord.Intents.all())
@commands.has_permissions(manage_messages=True)

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def warn(ctx, member: nextcord.Member, *, reason=None):
        warn_channel = bot.get_channel(1082378325567217727)
        await warn_channel.send(f"{member.mention} figyelmeztetve lett. Ok: {reason}")

def setup(bot):
    bot.add_cog(Warn(bot))