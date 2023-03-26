import nextcord
import os
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import commands, application_checks

intents = nextcord.Intents.default()

intents.message_content = True
intents.typing = True
intents.presences = True
intents.members=True
intents.guilds=True
intents.voice_states=True
intents.messages = True
intents.bans = True
intents.dm_messages = True
intents.reactions = True
intents.messages = True
intents.guilds = True
intents.reactions = True


bot = commands.Bot(command_prefix='-', help_command=None, intents=intents)

bot.load_extension("CommandHandler")

def is_me(ctx: Interaction):
    return ctx.message.author.id == 864583234158460938 or ctx.message.author.id == 1056315640048263230

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Bejelentkezve mint: {0} ({0.id})'.format(bot.user))
    await bot.change_presence(activity=nextcord.Game(name="Natsuki#5480 csicskája"))

@bot.slash_command(name="reloadcommands", description="Reloads the CommandHandler")
@application_checks.check(is_me)
async def reloadcommands(ctx: Interaction):
    await ctx.send("Reloading CommandHandler")
    bot.reload_extension("CommandHandler")


bot.run('MTA4MjMxMjk2ODUyNTU4MjQ2Nw.GSLtzn.vSylb0vNEt1Ry3LLOHyQbiULjm9IGCBLKkbfds')