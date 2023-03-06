import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='t!')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
@bot.event
async def on_ready():
    print('Bejelentkezve mint: {0} ({0.id})'.format(bot.user))
    await bot.change_presence(activity=discord.Game(name="Kezdésnek írd be, hogy: t!segitseg"))

bot.run('MTA4MjMxMjk2ODUyNTU4MjQ2Nw.GSLtzn.vSylb0vNEt1Ry3LLOHyQbiULjm9IGCBLKkbfds')