import nextcord
from nextcord import Interaction, SlashOption
import random
from datetime import datetime
from nextcord.ext import commands, application_checks

intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix = ".ds ", help_command = None, intents = intents)

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
    async def dice(self, ctx : Interaction, dice: str = SlashOption(description="Dobj kockával. Például: 1k6  azaz egy kockával dobsz hatszor")):
        """Az elfogadott formátum 1k6"""
        try:
            rolls, limit = map(int, dice.split('k'))
        except Exception:
            await ctx.send('A formátumnak `NkN`-nek kell lennie!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

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

    @bot.slash_command(name ="help", description="A bot parancsait mutatja meg")
    async def help(self,ctx : Interaction):

        #Játék parancsok
        MyEmbed = nextcord.Embed(title = "Játék parancsok", description = "Itt vannak a bot játékai!", color = nextcord.Colour.orange())
        MyEmbed.set_thumbnail(url = "https://i.pinimg.com/originals/40/b4/69/40b469afa11db730d3b9ffd57e9a3af9.jpg")
        MyEmbed.add_field(name = "/ping", value = "A bot ezzel fog válaszolni: Pong!", inline = False)
        MyEmbed.add_field(name = "/dice", value = "Ezzel a paranccsal tudsz dobókockával dobni.", inline = False)
        MyEmbed.add_field(name = "/coinflip", value = "This command lets you flip a coin", inline = False)
        MyEmbed.add_field(name = "/rps ✌️/🤜/✋", value = "Ezzel a paranccsal tudsz kő papír ollót játszani a bottal", inline = False)
        
        #Zene parancsok
        MusicEmbed = nextcord.Embed(title = "Zene prancsok", description = "Itt vannak a bot zene parancsai.", color = nextcord.Colour.orange())
        MusicEmbed.set_thumbnail(url = "https://i.pinimg.com/originals/40/b4/69/40b469afa11db730d3b9ffd57e9a3af9.jpg")
        MusicEmbed.add_field(name = "/join", value = "Ezzel a paranccsal fog a bot belépni abba a szobába amelyikben vagy! ", inline = False)
        MusicEmbed.add_field(name = "/play", value = "Ezzel a paranccsal fogsz tudni zenét lejátszani! ", inline = False)
        MusicEmbed.add_field(name = "/skip", value = "Ezzel a paranccsal nyomod tovább a zenét!", inline = False)
        MusicEmbed.add_field(name = "/pause", value = "Ez megállítja az éppen játszott zenét!", inline = False)
        MusicEmbed.add_field(name = "/resume", value = "Folyatódik a zene!", inline = False)
        MusicEmbed.add_field(name = "/stop", value = "Megállítja a jelenlegi zenét!", inline = False)
        MusicEmbed.add_field(name = "/queue", value = "Ezzel a paranccsal meg tudod nézni milyen zenék vannak a lejátszási listán, ha több zenét is lejátszik!", inline = False)
        
        #Moderációs parancsok
        ModEmbed = nextcord.Embed(title = "Moderációs parancsok", description = "Ezek a bot moderációs parancsai", color = nextcord.Colour.orange())
        ModEmbed.set_thumbnail(url = "https://i.pinimg.com/originals/40/b4/69/40b469afa11db730d3b9ffd57e9a3af9.jpg")
        #ModEmbed.add_field(name = "/servername", value = "Edits the server name!", inline = False)
        #ModEmbed.add_field(name = "/region", value = "Edits the server Region!", inline = False)
        ModEmbed.add_field(name = "/createrole", value = "Egy rangot fog készíteni!", inline = False)
        ModEmbed.add_field(name = "/createtextchannel és /createvoicechannel", value = "Készít egy szöveges/hangcsatornát!", inline = False)
        ModEmbed.add_field(name = "/ban @felhasználó", value = "Kitíltja a felhasználót a szerverről!", inline = False)
        ModEmbed.add_field(name = "/kick @felhasználó", value = "Kirúgja az adott felhasználót a szerverrről!", inline = False)
        ModEmbed.add_field(name = "/mute @felhasználó", value = "Némítja a felhasználót!", inline = False)
        ModEmbed.add_field(name = "/deafen @felhasználór", value = "Sűketíti a felhasználót egy hangcsatornában!", inline = False)
        ModEmbed.add_field(name = "/purge szám", value = "X mennyiségű üzenetet fog törölni!", inline = False)
        ModEmbed.add_field(name = "/unban felhasználó#XXXX", value = "Ezzel a paranccsal visszavonod a parancsot!", inline = False)
        ModEmbed.add_field(name = "/unmute/undeafen @felhasználó", value = "Unmutes/Undeafens a user in a Voice Channel!", inline = False)
        ModEmbed.add_field(name = "/voicekick @felhasználó", value = "Kirúgja a felhasználót a ", inline = False)
        
        #parancsok elküldése privát üzenetben
        await ctx.send("Nézd meg a privát üzeneteid!")
        await ctx.user.create_dm()
        await ctx.user.dm_channel.send(embed = MyEmbed)
        await ctx.user.dm_channel.send(embed = MusicEmbed) 
        await ctx.user.dm_channel.send(embed = ModEmbed)   

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

    #Moderációs parancsok

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