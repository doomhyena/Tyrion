import nextcord
from nextcord.ext import commands
prefix = '-'

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        
        #Játék parancsok
        MyEmbed = nextcord.Embed(title = "Játék parancsok", description = "Itt vannak a bot játékai!", color = nextcord.Colour.orange())
        MyEmbed.add_field(name = f"{prefix}ping", value = "A bot ezzel fog válaszolni: Pong!", inline = False)
        MyEmbed.add_field(name = f"{prefix}dice", value = "Ezzel a paranccsal tudsz dobókockával dobni.", inline = False)
        MyEmbed.add_field(name = f"{prefix}coinflip", value = "This command lets you flip a coin", inline = False)
        MyEmbed.add_field(name = f"{prefix}rps ✌️/🤜/✋", value = "Ezzel a paranccsal tudsz kő papír ollót játszani a bottal", inline = False)
        
        #Zene parancsok
        MusicEmbed = nextcord.Embed(title = "Zene prancsok", description = "Itt vannak a bot zene parancsai.", color = nextcord.Colour.orange())
        MusicEmbed.add_field(name = f"{prefix}join", value = "Ezzel a paranccsal fog a bot belépni abba a szobába amelyikben vagy! ", inline = False)
        MusicEmbed.add_field(name = f"{prefix}play", value = "Ezzel a paranccsal fogsz tudni zenét lejátszani! ", inline = False)
        MusicEmbed.add_field(name = f"{prefix}skip", value = "Ezzel a paranccsal nyomod tovább a zenét!", inline = False)
        MusicEmbed.add_field(name = f"{prefix}pause", value = "Ez megállítja az éppen játszott zenét!", inline = False)
        MusicEmbed.add_field(name = f"{prefix}resume", value = "Folyatódik a zene!", inline = False)
        MusicEmbed.add_field(name = f"{prefix}stop", value = "Megállítja a jelenlegi zenét!", inline = False)
        MusicEmbed.add_field(name = f"{prefix}queue", value = "Ezzel a paranccsal meg tudod nézni milyen zenék vannak a lejátszási listán, ha több zenét is lejátszik!", inline = False)
        
        #Moderációs parancsok
        ModEmbed = nextcord.Embed(title = "Moderációs parancsok", description = "Ezek a bot moderációs parancsai", color = nextcord.Colour.orange())
        ModEmbed.add_field(name = f"{prefix}ban @felhasználó", value = "Kitíltja a felhasználót a szerverről!", inline = False)
        ModEmbed.add_field(name = f"{prefix}kick @felhasználó", value = "Kirúgja az adott felhasználót a szerverrről!", inline = False)
        ModEmbed.add_field(name = f"{prefix}mute @felhasználó", value = "Némítja a felhasználót!", inline = False)
        ModEmbed.add_field(name = f"{prefix}deafen @felhasználór", value = "Sűketíti a felhasználót egy hangcsatornában!", inline = False)
        ModEmbed.add_field(name = f"{prefix}purge szám", value = "X mennyiségű üzenetet fog törölni!", inline = False)
        ModEmbed.add_field(name = f"{prefix}unban felhasználó#XXXX", value = "Ezzel a paranccsal visszavonod a parancsot!", inline = False)
        ModEmbed.add_field(name = f"{prefix}timeout felhasználó#XXXX", value = "Időkorlátozza a felhasználót!", inline = False)
        ModEmbed.add_field(name = f"{prefix}removetimeout felhasználó#XXXX", value = "Leveszi az időkorlátozást a felhasználóról!", inline = False)
        ModEmbed.add_field(name = f"{prefix}voicekick @felhasználó", value = "Kirúgja a felhasználót a ", inline = False)
        
        #parancsok elküldése privát üzenetben
        await ctx.send(embed = MyEmbed)
        await ctx.send(embed = MusicEmbed) 
        await ctx.send(embed = ModEmbed)  

def setup(bot):
    bot.add_cog(Help(bot))