import nextcord
from nextcord import Interaction, SlashOption
import random
from datetime import datetime
from nextcord.ext import commands, application_checks

intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix = "-", help_command = None, intents = intents)

class CommandHandler(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    #Játék parancsok
    @bot.slash_command(name= "ping", description="A bot pingjét írja ki")
    async def ping(self, ctx : Interaction):
        await ctx.send(f"Pong! 🏓  {self.bot.latency * 1000:.0f}ms")

    @bot.slash_command(description="Pénz dobás")
    async def coinflip(self,ctx : Interaction):
        num = random.randint(1, 2)
        if num == 1:
            await ctx.send("Fej!")
        if num == 2:
            await ctx.send("Írás!")

    @bot.slash_command(name = "dice", description="Dobj kockával. Például: 1k6  azaz egy kockával dobsz hatszor")
    async def dice(self, ctx : Interaction):
        await ctx.send(f"🎲 {random.randint(1, 6)}")

    @bot.slash_command(name = "rps", description="Kő papír olló játék")
    async def rps(self,ctx : Interaction, hand : str = SlashOption(description="Válassz ezek közül: ✌️, ✋ vagy 🤜")):

        hands = ["✌️","✋","🤜"]
        handExist = hand in hands
        bothand = random.choice(hands)

        if handExist:
            await ctx.send(bothand)
            if hand == bothand:    
                await ctx.send("Ez egyenlő!")

            elif hand == "✌️":
                if bothand == "🤜":
                    await ctx.send("Én nyertem!")
                if bothand == "✋":
                    await ctx.send("Te nyertél!")

            elif hand == "✋":
                if bothand == "✌️":
                    await ctx.send("Én nyertem!")
                if bothand == "🤜":
                     await ctx.send("Te nyertél")        

            elif hand == "🤜":
                if bothand == "✋":
                    await ctx.send("Én nyertem!")
                if bothand == "✌️":
                    await ctx.send("Te nyertél!") 

        else: 
            await ctx.send("Kérlek játsz helyesen")

    #Szerver készítéséhez való parancsok

    @bot.slash_command(name="createtextchannel", description="Egy szöveges csatornát készít")
    @application_checks.has_permissions(manage_guild = True)
    async def createtextchannel(self,ctx : Interaction,*,input : str = SlashOption(description="Csatorna név")):
        await ctx.guild.create_text_channel(name = input)
        await ctx.send(f"A szöveges csatorna elkészítve, {input}")

    @bot.slash_command(name="createvoicechannel", description="Egy hangcsatornát készít")
    @application_checks.has_permissions(manage_guild = True)
    async def createvoicechannel(self,ctx : Interaction,*,input : str = SlashOption(description="Csatorna név")):
        await ctx.guild.create_voice_channel(name = input)
        await ctx.send(f"A szöveges csatorna elkészítve, {input}")

    @bot.slash_command(name="createrole", description="Egy rangot készít")
    @application_checks.has_permissions(manage_guild = True)
    async def createrole(self,ctx : Interaction,*,input : str = SlashOption(description="Rang név")):
        await ctx.guild.create_role(name = input)
        await ctx.send(f"A rang elkészítve, {input}")

    #----------------------------------------------//----------------------------------------------#
    #Moderációs parancsok  

    @bot.slash_command(name="kick", description="Kirúg egy felhasználót")
    @application_checks.has_permissions(kick_members = True)
    async def kick(self,ctx : Interaction, member : nextcord.Member, *, reason = SlashOption(description="A kirúgás indoka")):
        await ctx.guild.kick(member, reason = reason)
        await ctx.send(f"{member}, sikeresen kirúgva ezzel az indokkal: {reason}.")

    @bot.slash_command(name="ban", description="Kitílt egy felhasználót")
    @application_checks.has_permissions(ban_members = True)
    async def ban(self,ctx : Interaction, member : nextcord.Member, *, reason = SlashOption(description="A kitíltás indoka")):
        await ctx.guild.ban(member, reason = reason)
        await ctx.send(f"{member} sikeresen kitíltva ezzel az indokkal: {reason}.")

    @bot.slash_command(name="unban", description="Feloldja a kitíltást")
    @application_checks.has_permissions(ban_members = True)
    async def unban(self,ctx : Interaction, *,input : str = SlashOption(description="Felhasználó#XXXX")):
        name, discriminator = input.split("#")
        banned_members = await ctx.guild.bans()
        for bannedmember in banned_members:
            username = bannedmember.user.name
            disc = bannedmember.user.discriminator
            if name == username and discriminator == disc:
                await ctx.guild.unban(bannedmember.user)
                await ctx.send(f"A felhasználó, {username}#{disc} sikeresen feloldva.")
                
    @bot.slash_command(name="purge", description="X mennyiségű üzenetet töröl ki.")
    @application_checks.has_permissions(manage_messages = True)
    async def purge(self,ctx : Interaction, amount = SlashOption(description="üzenetmennyiség"), day : int = None , month : int = None, year : int = datetime.now().year):
        if amount == "/":
            if day == None or month == None:
                return
            else:
                await ctx.channel.purge(after = datetime(year, month, day))
                await ctx.send(f"Törölted az összes üzenetet, {day}/{month}/{year}")
        else:
            await ctx.channel.purge(limit = int(amount) + 1)
            await ctx.send(f"Kitöröltél {amount} üzenetet.")

    @bot.slash_command(name="mute", description="Lenémítja a felhasználót")
    @application_checks.has_permissions(mute_members = True)
    async def mute(self, ctx : Interaction, user : nextcord.Member = SlashOption(description="Felhasználó lenémítása")):
        await user.edit(mute = True)
        await ctx.send(f"Muted {user}")

    @bot.slash_command(name="unmute", description="Feloldja a felhasználót a némítás alól.")
    @application_checks.has_permissions(mute_members = True)
    async def unmute(self,ctx : Interaction, user : nextcord.Member = SlashOption(description="Feloldja a felhasználót a némítás alól.")):
        await user.edit(mute = False)
        await ctx.send(f"A felhasználó sikeresen feloldva a némítás alól, {user}.")

    @bot.slash_command(name="deafen", description="Süketíti a felhasználót.")
    @application_checks.has_permissions(deafen_members = True)
    async def deafen(self,ctx : Interaction, user : nextcord.Member = SlashOption(description="Süketíti a felhasználót.")):
        await user.edit(deafen = True)
        await ctx.send(f"A felhasználó sikeresen sűketítve, {user}.")

    @bot.slash_command(name="undeafen", description="Feloldja a süketítés alól a felhasználót.")
    @application_checks.has_permissions(deafen_members = True)
    async def undeafen(self,ctx : Interaction, user : nextcord.Member = SlashOption(description="Feloldja a süketítés alól a felhasználót.")):
        await user.edit(deafen = False)
        await ctx.send(f"Undeafened {user}")

    @bot.slash_command(name="voicekick", description="Kirúgja a felhasználót a hangcsatornából.")
    @application_checks.has_permissions(kick_members = True)
    async def voicekick(self,ctx : Interaction, user : nextcord.Member = SlashOption(description="Kirúgja a felhasználót a hangcsatornából.")):
        await user.edit(voice_channel = None)
        await ctx.send(f"{user} kirúgva a hangcsatornából.")

    #----------------------------------------------//----------------------------------------------#
    #Hiba üzenetek

    #Játék parancsok 
    @rps.error
    async def errorhandler(self, ctx : Interaction, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Kérlek válassz ✌️/🤜/✋")

    #Moderációs

    @createtextchannel.error
    async def errorhandler(self, ctx : Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nincs elég jogosultságod hozzá!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Kérlek adjál meg egy csatornát!")

    @createvoicechannel.error
    async def errorhandler(self, ctx : Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nincs elég jogosultságod hozzá!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Kérlek adjál meg egy csatornát!")

    @kick.error
    async def errorhandler(self,ctx : Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nincs elég jogosultságod hozzá!")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Kérlek jelölj meg egy felhasználót!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("A parancs használatához meg kell említenie egy felhasználót!")

    @ban.error
    async def errorhandler(self,ctx : Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nincs elég jogosultságod hozzá!")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Kérlek jelölj meg egy felhasználót!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("A parancs használatához meg kell említenie egy felhasználót!")

    @purge.error
    async def errorhandler(self,ctx : Interaction, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("meg kell adnia egy dátumot vagy egy üzenetszámot!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Csak egy / vagy egy számot lehet 1. beírni.")

        
def setup(bot):
    bot.add_cog(CommandHandler(bot))