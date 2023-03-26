import nextcord
from nextcord import *
from nextcord.ext import commands
import datetime
import json

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx, csatorna: nextcord.TextChannel):
        components1 = [ Button(label=":ticket:"), Button(label=":lock:") ]
        embed=nextcord.Embed(title="Ticket", description="Reagálj a :ticket: emojival a ticket létrehozásához!", color=0xff9900)
        embed.set_footer(icon_url=self.client.user.avatar_url, text="Radon × Ticket")
        global msg
        msg = await csatorna.send(embed=embed, components=components1[0])
        interaction = await self.client.wait_for("button_click")
        if interaction:
            with open("data.json") as f: data = json.load(f)
            ticket_number = int(data["ticket-counter"])
            ticket_number += 1
            ticket_channel = await interaction.guild.create_text_channel(f"ticket-{interaction.author}")
            await ticket_channel.set_permissions(interaction.guild.get_role(interaction.guild.id), send_messages=False, read_messages=False)
            for role_id in data["valid-roles"]:
                role = interaction.guild.get_role(role_id)
                await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True, manage_channel=True)
            await ticket_channel.set_permissions(interaction.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
            tmsg=await ticket_channel.send(f"{interaction.author.mention}, a ticketed elkészült! Lezárás a :lock: emojival.", components=components1[1])
            pinged_msg_content = ""
            non_mentionable_roles = []
            if data["pinged-roles"] != []:
                for role_id in data["pinged-roles"]:
                    role = interaction.guild.get_role(role_id)
                    pinged_msg_content += role.mention
                    pinged_msg_content += " "
                    if role.mentionable: pass
                else: await role.edit(mentionable=True); non_mentionable_roles.append(role)
                await ticket_channel.send(pinged_msg_content)
                for role in non_mentionable_roles: await role.edit(mentionable=False)
            data["ticket-channel-ids"].append(ticket_channel.id)
            data["ticket-counter"] = int(ticket_number)
            with open("data.json", 'w') as f: json.dump(data, f)
            created_em = nextcord.Embed(description="Sikeres létrehozás ({})".format(ticket_channel.mention), timestamp=datetime.datetime.utcnow(), color=0xFF9900)
            created_em.set_author(name=f"Ticket", icon_url=interaction.author.avatar_url)
            await interaction.author.send(embed=created_em)
            reaction2 = await self.client.wait_for("button_click")
            if reaction2=="🔒":
                with open('data.json') as f: data = json.load(f)
                if interaction.channel.id in data["ticket-channel-ids"]: channel_id = interaction.channel.id
                await interaction.channel.delete()
                index = data["ticket-channel-ids"].index(channel_id)
                del data["ticket-channel-ids"][index]
                with open('data.json', 'w') as f: json.dump(data, f)

def setup(bot):
    bot.add_cog(Ticket(bot))
