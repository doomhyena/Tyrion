import nextcord
import os
import datetime
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.ext import commands, application_checks

intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix='-', intents=intents)

bot.remove_command("help")

def is_me(ctx: Interaction):
    return ctx.message.author.id == 864583234158460938 or ctx.message.author.id == 1056315640048263230

@bot.event
async def on_ready():
    print('Bejelentkezve mint: {0} ({0.id})'.format(bot.user))
    await bot.change_presence(activity=nextcord.Game(name="Kezdésnek írd be, hogy: -help"))

@bot.event
async def on_command_error(ctx, error):
    command = bot.get_command(str(ctx.message.content).replace(",", ""))
    if isinstance(error, commands.MissingRequiredArgument):
        if command is None:
            return
        if command.usage == None: command.usage = "Nincs használat megadva."
        embed = nextcord.Embed(title="Helytelen használat!", description=f"`Használat: {command.usage}`", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.BotMissingPermissions):
        embed = nextcord.Embed(title="Hiányzó jogosultság", description=f"A botnak nincs elegendő jogosultsága!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)

    elif isinstance(error, commands.BadArgument):
        if command.usage == None: command.usage = "Nincs használat megadva."
        embed = nextcord.Embed(title="Helytelen használat!", description=f"`Használat: {command.usage}`", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.CommandOnCooldown):
        cd = round(error.retry_after)
        minutes = str(cd // 60)
        seconds = str(cd % 60)
        days = str(round((error.retry_after/86400000),2))
        embed = nextcord.Embed(title="Hiba történt!", description=f"Még nem használhatod ezt a parancsot! Hátralévő idő `{minutes}` perc, `{seconds}` másodperc", color=nextcord.Colour.orange(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, AttributeError):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ismeretlen hiba történt! `{error}`", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(title="Hiba", description=f"Nincs jogod a parancs használatához! Ehhez kell: `{error.missing_perms}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Rebus × Hiányzó jog", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, mention_author=False)
    elif isinstance(error, commands.ChannelNotFound):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ez a csatorna nem található!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.EmojiNotFound):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ez az emotikon nem található!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.MemberNotFound):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ez a felhasználó nem található!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.RoleNotFound):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ez a rang nem található!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, commands.UserNotFound):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Ez a felhasználó nem található!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, nextcord.Forbidden):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Nincs elegendő jogom ezt a felhasználót kezelni!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)
    elif isinstance(error, nextcord.errors.Forbidden):
        embed = nextcord.Embed(title="Hiba történt!", description=f"Nincs elegendő jogom ezt a felhasználót kezelni!", color=nextcord.Colour.red(), timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed, mention_author=False)     

    else:
        raise error
for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try: bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e: 
                print(f"Hiba történt!\n{e}")

import sys

async def setup():
    print("[INFO] ~> Parancsfájlok betöltése")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try: bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e: 
                print(f"Hiba történt!\n{e}")
                sys.exit()


@bot.slash_command(name="reloadcommands", description="Reloads the CommandHandler")
@application_checks.check(is_me)
async def reloadcommands(ctx: Interaction):
    await ctx.send("Reloading CommandHandler")
    bot.reload_extension("CommandHandler")


# bot.run('MTAyOTA2MjAyMTU0MDQ3OTA0Ng.GQQgeu.XN5sPSbFwUNCX-QEg02Y3AmoUZUIyKjhdkfnGc') Dev Bot
bot.run('MTA4MjMxMjk2ODUyNTU4MjQ2Nw.GSLtzn.vSylb0vNEt1Ry3LLOHyQbiULjm9IGCBLKkbfds')