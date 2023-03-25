import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix='t!', intents= nextcord.Intents.all())
@commands.has_permissions(manage_roles=True)

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commands.command()
    async def mute(ctx, member: nextcord.Member, *, reason=None):
        role = nextcord.utils.get(ctx.guild.roles, name="Némított") 
        if not role:
            role = await ctx.guild.create_role(name="Némított")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=True)

            await member.add_roles(role, reason=reason)
            await ctx.send(f"{member.mention} el lett némítva. Ok: {reason}")


def setup(bot):
    bot.add_cog(Mute(bot))