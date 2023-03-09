from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="help", aliases=["commands"])
    async def help_command(self, ctx):
        """Parancsok listázása"""

        embed = discord.Embed(title="Parancsok listája", description="Itt találod a használható parancsokat:", color=0x00ff00)
        
        for cog in self.client.cogs:
            cog_commands = self.client.get_cog(cog).get_commands()
            command_list = [command for command in cog_commands if not command.hidden]
            if command_list:
                command_names = [command.name for command in command_list]
                command_descs = [command.help for command in command_list]
                embed.add_field(name=cog, value="\n".join(f"`{name}` - {desc}" for name, desc in zip(command_names, command_descs)), inline=False)
        
        await ctx.send(embed=embed)
