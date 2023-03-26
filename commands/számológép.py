import nextcord
from nextcord import *
from nextcord.ext import commands


class SzMolGP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["számológép","btncalc","gombszámológép","buttoncalculator","buttoncalc","gombszámoló"])
    async def szamologep(self, ctx):
        if not ctx.author.id == 406137394228625419: return
        numbers = []
        muvelet = []
        components = [
            [ Button(label="7"), Button(label="8"), Button(label="9"), Button(label="÷", style=ButtonStyle.blue)  ],
            [ Button(label="4"), Button(label="5"), Button(label="6"), Button(label="*", style=ButtonStyle.blue)  ], 
            [ Button(label="1"), Button(label="2"), Button(label="3"), Button(label="-", style=ButtonStyle.blue) ],
            [ Button(label="X", style=ButtonStyle.red), Button(label="0"), Button(label="=", style=ButtonStyle.green), Button(label="+", style=ButtonStyle.blue) ],
            [ Button(label=",", style=ButtonStyle.blue), Button(label="C", style=ButtonStyle.blue), Button(label="AC", style=ButtonStyle.blue), Button(label="INFÓ", style=ButtonStyle.blue) ]
        ]
        embed = nextcord.Embed(description="``` 0 ```", color=0xff9900)
        embed.set_author(name="Számológép", icon_url=ctx.author.avatar_url)
        
        msg = await ctx.reply(embed=embed, components=components, mention_author=False)
        
        while True:
            interaction = await self.client.wait_for("button_click", check = lambda i: i.author.id == ctx.author.id)
            nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            if interaction.component.label in nums: numbers.append(interaction.component.label)
            else: 
                if interaction.component.label == "÷":
                    muvelet.append("/")
                else: muvelet.append(interaction.component.label)
            if len(muvelet) == 0: embed = nextcord.Embed(title="Számológép", description=f"``` {numbers[0]} ```")
            else: 
                try: embed = nextcord.Embed(title="Számológép", description=f"``` {numbers[0]} {muvelet[0]} {numbers[1]} ```")
                except: embed = nextcord.Embed(title="Számológép", description=f"``` {numbers[0]} {muvelet[0]} ```")
            if interaction.component.label == "=":
                if muvelet[0] == "/":
                    eredmeny = int(numbers[0]) / int(numbers[1])
                    embed = nextcord.Embed(title="Számológép", description=f"``` {eredmeny} ```")
                    await interaction.respond(type=InteractionType.UpdateMessage, content=None, embed=embed, components=components)
                    numbers.clear()
                    muvelet.clear()
                if muvelet[0] == "+":
                    eredmeny = int(numbers[0]) + int(numbers[1])
                    embed = nextcord.Embed(title="Számológép", description=f"``` {eredmeny} ```")
                    await interaction.respond(type=InteractionType.UpdateMessage, content=None, embed=embed, components=components)
                    numbers.clear()
                    muvelet.clear()
                if muvelet[0] == "-":
                    eredmeny = int(numbers[0]) - int(numbers[1])
                    embed = nextcord.Embed(title="Számológép", description=f"``` {eredmeny} ```")
                    await interaction.respond(type=InteractionType.UpdateMessage, content=None, embed=embed, components=components)
                    numbers.clear()
                    muvelet.clear()
                if muvelet[0] == "*":
                    eredmeny = int(numbers[0]) * int(numbers[1])
                    embed = nextcord.Embed(title="Számológép", description=f"``` {eredmeny} ```")
                    await interaction.respond(type=InteractionType.UpdateMessage, content=None, embed=embed, components=components)
                    numbers.clear()
                    muvelet.clear()
                
            else:
                await interaction.respond(type=InteractionType.UpdateMessage, content=None, embed=embed, components=components)

def setup(bot):
    bot.add_cog(SzMolGP(bot))
