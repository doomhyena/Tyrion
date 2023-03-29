import nextcord
import datetime
import inspect
import asyncio
import convert
import json
import random
import psutil
import platform
from nextcord import *
from nextcord.ext import commands
from nextcord.ui import Button, View, Select
from typing import Optional, Set

intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix = "-", help_command = None, intents = intents)


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Moderációs parancsok
    @commands.command(usage="addrole [@említés] [@rang]")
    async def addrole(self, ctx, user, *, role):   
        if ctx.author.guild_permissions.manage_roles == False: 
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            try: user = await commands.MemberConverter().convert(ctx, user)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            try: role = await commands.RoleConverter().convert(ctx, role)
            except:
                embed = nextcord.Embed(description="Nem található ilyen rang a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed = embed, mention_author=False)
                return
            if ctx.author.id == user.id: 
                embed = nextcord.Embed(description="Nem adhatsz magadnak rangot!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            elif ctx.author.guild.owner == False:
                if ctx.author.top_role < role: 
                    embed = nextcord.Embed(description="Ez a rang magasabb mint a te rangod, ezért nem adhatod oda másnak!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            else:
                pass
            bot = await commands.MemberConverter().convert(ctx, str(713014602891264051))
            if bot.guild_permissions.manage_roles == False: 
                embed = nextcord.Embed(description="Nincs jogosultságom a felhasználó kezelésére!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            await user.add_roles(role)
            embed = nextcord.Embed(description=f":white_check_mark: {role.mention} sikeresen odaadva {user.mention} számára!", timestamp = datetime.datetime.utcnow(), color=0xff9900)
            embed.set_author(name="Rang adás", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{ctx.author} × Rang adás", icon_url=self.bot.user.display_avatar)
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(usage="ban [felhasználó] (indok)", aliases=["kitilt", "kitiltás", "kitiltas"])
    async def ban(self, ctx, member, *, reason):
        if ctx.author.guild_permissions.ban_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.client.user.avatar_url)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod kitiltani!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply(" A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.ban_members: await ctx.reply("A botnak nincs joga kitiltáshoz!", mention_author=False); return
            else:
                try:
                    embed = nextcord.Embed(description=f"Ki lettél tiltva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed.add_field(name="Általa", value=ctx.author, inline=False)
                    embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                    embed.set_author(name="Ki lettél tiltva!", icon_url=ctx.guild.icon_url)
                    embed.set_footer(text="Radon × Kitiltás", icon_url=self.bot.user.display_avatar)
                    await member.send(embed=embed)
                except: pass
                await ctx.guild.ban(user=member, reason=reason, delete_message_days=0)
                embed2 = nextcord.Embed(description=f"**{member.name}** ki lett tiltva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                embed2.add_field(name="Indok", value=f"`{reason}`")
                embed2.set_author(name="Sikeres kitiltás!", icon_url=ctx.author.display_avatar)
                embed2.set_footer(text=f"{ctx.author.name} × Kitiltás", icon_url=self.bot.user.display_avatar)
                await ctx.send(embed=embed2)
        else:
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

    commands.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} üzenet törölve.")

    @commands.command(aliases=["nick", "setnick"])
    async def setnickname(self, ctx, member: nextcord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Siekresen megváltoztattam {member.mention} felhasználónak a nevét!')

    @commands.command(usage="kick [felhasználó] (indok)", aliases=["kirúg", "kirug", "kirugás", "kirúgás", "kirúgas"])
    async def kick(self, ctx, member, *, reason="Nincs indok megadva."):
        if ctx.author.guild_permissions.kick_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod kirúgni!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply("A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.kick_members: await ctx.reply("A botnak nincs joga kirúgáshoz!", mention_author=False); return
            else:
                try:
                    embed = nextcord.Embed(description=f"Ki lettél rúgva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed.add_field(name="Általa", value=ctx.author, inline=False)
                    embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                    embed.set_author(name="Ki lettél rúgva!", icon_url=ctx.author.display_avatar)
                    embed.set_footer(text="Rebus × Kirúgás", icon_url=self.client.user.display_avatar)
                    await member.send(embed=embed)
                except: pass
                await ctx.guild.kick(user=member, reason=reason)
                embed2 = nextcord.Embed(description=f"**{member.name}** ki lett rúgva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                embed2.add_field(name="Indok", value=f"`{reason}`")
                embed2.set_author(name="Sikeres kirúgás!", icon_url=ctx.author.display_avatar)
                embed2.set_footer(text=f"{ctx.author.name} x Kirúgás", icon_url=self.client.user.display_avatar)
                await ctx.send(embed=embed2)
        else:
            perm = "Tagok kirúgása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

    @commands.command(usage="mute <felhasználó> [indok: opcionális]")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: nextcord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = nextcord.utils.get(guild.roles, name="Némított")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Némított")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
                await asyncio.sleep(2)
        embed = nextcord.Embed(title="Némítás", description=f"{member.mention} sikeresen le lett némítva ", colour=nextcord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"Le lettél némítva a **{guild.name}** szerveren!\n Indok: **{reason}**")

    @commands.command(usage="removerole [@említés] [@rang]")
    async def removerole(self, ctx, user, *, role):   
        if ctx.author.guild_permissions.manage_roles == False: 
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            try: user = await commands.MemberConverter().convert(ctx, user)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            try: role = await commands.RoleConverter().convert(ctx, role)
            except:
                embed = nextcord.Embed(description="Nem található ilyen rang a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.send(embed = embed, mention_author=False)
                return
            if ctx.author.id == user.id: 
                embed = nextcord.Embed(description="Nem vehetsz le magadról rangot!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            elif ctx.author.guild.owner == False:
                if ctx.author.top_role < role: 
                    embed = nextcord.Embed(description="Ez a rang magasabb mint a te rangod, ezért nem veheted le másról!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            else:
                pass
            bot = await commands.MemberConverter().convert(ctx, str(713014602891264051))
            if bot.guild_permissions.manage_roles == False: 
                embed = nextcord.Embed(description="Nincs jogosultságom a felhasználó kezelésére!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed, mention_author=False)
                return
            await user.remove_roles(role)
            embed = nextcord.Embed(description=f":white_check_mark:{role.mention} sikeresen elvéve {user.mention}-tól/-től!", timestamp = datetime.datetime.utcnow(), color=0xff9900)
            embed.set_author(name="Rang elvétel", icon_url=ctx.author.avatar_url)
            embed.set_footer(text=f"{ctx.author} × Rang elvétel", icon_url=self.client.user.display_avatar)
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(usage="removeroleall [@rang]", aliases=["removeall"])
    async def removeroleall(self, ctx, role):
        if ctx.author.guild_permissions.manage_roles:
            role = await commands.RoleConverter().convert(ctx, role)
            await ctx.reply("Kérlek várj...")
            for member in ctx.guild.members:
                try: await member.remove_roles(role)
                except: continue
                await asyncio.sleep(1)
            await ctx.send(f"Sikeresen elvettem az összes felhasználótól a {role.name} rangot!")
        else:
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)    

    @commands.command(usage="roleall [@rang]")
    async def roleall(self, ctx, role):
        if ctx.author.guild_permissions.manage_roles:
            role = await commands.RoleConverter().convert(ctx, role)
            await ctx.reply("Kérlek várj...")
            for member in ctx.guild.members:
                try: await member.add_roles(role)
                except: continue
                await asyncio.sleep(1)
            await ctx.send(f"Sikeresen megkapta az összes felhasználó a {role.name} rangot!")
        else:
            perm = "Rangok kezelése"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(usage="softban [felhasználó] (indok)")
    async def softban(self, ctx, member, *, reason):
        if ctx.author.guild_permissions.ban_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod kitiltani!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply("A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.ban_members: await ctx.reply("A botnak nincs joga kitiltáshoz!", mention_author=False); return
            else:
                try:
                    embed = nextcord.Embed(description=f"Ki lettél tiltva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed.add_field(name="Általa", value=ctx.author, inline=False)
                    embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                    embed.set_author(name="Ki lettél tiltva!", icon_url=ctx.guild.icon_url)
                    embed.set_footer(text="Radon × Kitiltás", icon_url=self.bot.user.display_avatar)
                    await member.send(embed=embed)
                except: pass
                await ctx.guild.ban(user=member, reason=reason, delete_message_days=7)
                embed2 = nextcord.Embed(description=f"**{member.name}** ki lett tiltva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                embed2.add_field(name="Indok", value=f"`{reason}`")
                embed2.set_author(name="Sikeres kitiltás!", icon_url=ctx.author.avatar_url)
                embed2.set_footer(text=f"{ctx.author.name} × Kitiltás", icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed2)
        else:
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

        @commands.command(usage="tempban [felhasználó] [idő] (indok)")
        async def tempban(self, ctx, member, ido, *, reason):
            if ctx.author.guild_permissions.ban_members:
                try: ido=convert(ido)
                except: await ctx.reply("Helytelen időformátum!", mention_author=False); return
                try: member = await commands.MemberConverter().convert(ctx, member)
                except: 
                    embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed1.set_author(name="Hiba!", icon_url=self.bot.user.display_avatar)
                    embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed1, mention_author=False)
                    return
                bot = await ctx.guild.fetch_member(1082312968525582467)
                if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod kitiltani!", mention_author=False); return
                if member.top_role >= ctx.author.top_role: await ctx.reply("A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
                if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
                if not bot.guild_permissions.ban_members: await ctx.reply("A botnak nincs joga kitiltáshoz!", mention_author=False); return
                else:
                    try:
                        embed = nextcord.Embed(description=f"Ki lettél tiltva a **{ctx.guild.name}** szerverről!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                        embed.add_field(name="Általa", value=ctx.author, inline=False)
                        embed.add_field(name="Indok", value=f"`{reason}`", inline=False)
                        embed.set_author(name="Ki lettél tiltva!", icon_url=ctx.guild.icon_url)
                        embed.set_footer(text="Radon × Kitiltás", icon_url=self.bot.user.display_avatar)
                        await member.send(embed=embed)
                    except: pass
                    await ctx.guild.ban(user=member, reason=reason, delete_message_days=0)
                    embed2 = nextcord.Embed(description=f"**{member.name}** ki lett tiltva **{ctx.author.name}** által!", timestamp=datetime.datetime.utcnow(), color=0xff9900)
                    embed2.add_field(name="Indok", value=f"`{reason}`")
                    embed2.set_author(name="Sikeres kitiltás!", icon_url=ctx.author.display_avatar)
                    embed2.set_footer(text=f"{ctx.author.name} × Kitiltás", icon_url=self.bot.user.display_avatar)
                    await ctx.send(embed=embed2)
                    await asyncio.sleep(ido)
                    await ctx.guild.unban(member)
            else:
                perm = "Tagok kitiltása"
                embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
                await ctx.reply(embed=embed, mention_author=False)
                return

    @commands.command(usage="tempmute [felhasználó] [idő] (indok)")
    async def tempmute(self, ctx, member, ido, *, reason="Nincs indok megadva"):
        if ctx.author.guild_permissions.kick_members:
            try: member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed1 = nextcord.Embed(description="Nem található ilyen felhasználó a szerveren!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed1.set_author(name="Hiba!", icon_url=self.client.user.avatar_url)
                embed1.set_footer(text=f"{ctx.author.name} × Hiba", icon_url=ctx.author.avatar_url)
                await ctx.reply(embed=embed1, mention_author=False)
                return
            bot = await ctx.guild.fetch_member(1082312968525582467)
            if member.id == ctx.author.id: await ctx.reply("Magadat nem tudod lenémítani!", mention_author=False); return
            if member.top_role >= ctx.author.top_role: await ctx.reply(" A felhasználónak van egy magasabb vagy ugyan olyan rangja, mint a te legfelső rangod!", mention_author=False); return
            if bot.top_role < member.top_role: await ctx.reply("A botnak kisebbek a rangjai, mint a felhasználónak!", mention_author=False); return
            if not bot.guild_permissions.manage_roles: await ctx.reply("A botnak nincs joga rangok adásához!", mention_author=False); return
            else:
                embed = nextcord.Embed(description=f"{member.mention} le lett némítva {ctx.author.mention} által!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name="Némítás", icon_url=ctx.author.display_avatar)
                embed.add_field(name="Indok", value=f"`{reason}`")
                embed.add_field(name="Időtartam", value=ido)
                embed.set_footer(text=f"{ctx.author.name} × Némítás", icon_url=self.bot.user.display_avatar)
                if not nextcord.utils.get(ctx.guild.roles, name="Némított"):
                    msg = await ctx.reply("Kérlek várj, amíg létrehozom a rangot és bekonfigurálom a rendszert...", mention_author=False)
                    mutedrole = await ctx.guild.create_role(name="Némított", colour=0xff9900, reason=f"Némítás - {ctx.author.name} - Egyszeri alkalom")
                    overwrites = {
                        mutedrole: nextcord.PermissionOverwrite(send_messages=False)
                    }
                    for i in ctx.guild.channels: await i.edit(overwrites=overwrites)
                    await msg.delete()
                try: ido=convert(ido)
                except: await ctx.reply("<:radon_x:856423841667743804> Helytelen időformátum!", mention_author=False); return
                await member.add_roles(nextcord.utils.get(ctx.guild.roles, name="Némított"))
                await ctx.reply(embed=embed, mention_author=False)
                await asyncio.sleep(ido)
                await member.remove_roles(nextcord.utils.get(ctx.guild.roles, name="Némított"))
        else:
            perm = "Tagok kirúgása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return


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

    @commands.command(usage="unban [felhasználónév és tag, pl. Radon#6074", aliases=["ub", "felold", "kitiltasfelold", "kitiltásfelold", "feloldás"])
    async def unban(self, ctx, user):
        if ctx.author.guild_permissions.ban_members == False: 
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
        else:
            if user.isdigit() == False: 
                lista = user.split('#')
                if len(lista) != 2: 
                    embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else: 
                    member_name = lista[0]
                    member_discriminator = lista[1]
                    banned_users = await ctx.guild.bans()
                    asd = False
                    for ban in banned_users:
                        if (ban.user.name, ban.user.discriminator) == (member_name, member_discriminator):
                            await ctx.guild.unban(ban.user)
                            embed = nextcord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xff9900, description = f"`{ban.user.name}#{ban.user.discriminator}` kitiltása `{ctx.author.name}#{ctx.author.discriminator}` által feloldásra került!")
                            embed.set_author(name="Kitiltás feloldása", icon_url=ctx.author.display_avatar)
                            embed.set_footer(text=f"{ctx.author} × Kitiltás feloldása", icon_url=self.client.user.display_avatarl)
                            await ctx.reply(embed=embed, mention_author=False)
                            asd = True
                            await user.send(f"A kitiltásod feloldották a **{ctx.author.guild_name}** szerveren!")
                    if asd == False:                         
                        embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                        await ctx.reply(embed=embed, mention_author=False)
                        return
            else:
                banned_users = await ctx.guild.bans()
                lista = [b.user.id for b in banned_users]
                if int(user) not in lista: 
                    embed = nextcord.Embed(description="Nem található ilyen felhasználó a kitiltottak listáján!", color=0xff9900, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name=f"Hiba × {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
                else:
                    user = await self.bot.fetch_user(user)
                    await ctx.guild.unban(user)
                    embed = nextcord.Embed(timestamp = datetime.datetime.utcnow(), color = 0xff9900, description = f"`{user.name}#{user.discriminator}` kitiltása `{ctx.author.name}#{ctx.author.discriminator}` által feloldásra került!")
                    embed.set_author(name="Kitiltás feloldása", icon_url=ctx.author.display_avatar)
                    embed.set_footer(text=f"{ctx.author} × Kitiltás feloldása", icon_url=self.bot.user.display_avatar)
                    await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def unbanall(self, ctx):
        if ctx.author.guild_permissions.ban_members:
            msg = await ctx.reply(content="Kérlek, várj...", mention_author=False)
            for member in await ctx.guild.bans():
                await ctx.guild.unban(member.user)
                await asyncio.sleep(2)
            await msg.edit("Sikeresen feloldottam az összes felhasználót!")
        else:
            perm = "Tagok kitiltása"
            embed = nextcord.Embed(title="Hiányzó jogok", description=f"Nincs elegendő jogod a parancs végrehajtásához!\nSzükséges jog: `{perm}`", color=nextcord.Color.red(), timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)
            return

    @commands.command(usage="unmute <felhasználó>")
    async def unmute(self, ctx, member: nextcord.Member):
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Némított")

        await member.remove_roles(mutedRole)
        await member.send(f"A némításod fel lett oldva a **{ctx.guild.name}** szerveren!")
        embed = nextcord.Embed(title="Némítás feloldása", description=f"Sikeresen feloldva {member.mention} a némítás alól",colour=nextcord.Colour.light_gray())
        await ctx.send(embed=embed)

    @commands.command()
    async def warn(ctx, member: nextcord.Member, *, reason=None):
        warn_channel = bot.get_channel(1082378325567217727)
        await warn_channel.send(f"{member.mention} figyelmeztetve lett. Ok: {reason}")

# Fun parancsok

    @commands.command()
    async def coinflip(ctx, amount=5):
        num = random.randint(1, 2)
        if num == 1:
            await ctx.send("Fej!")
        if num == 2:
            await ctx.send("Írás!")

    @commands.command(aliases=["dobokocka", "baszdfejbemagadat"])
    async def dice(self, ctx):
        await ctx.send(f"🎲 {random.randint(1, 6)}")

    @commands.command(usage="iq (@felhasználó)")
    async def iq(self, ctx, member=None):
        if member == None:
            embed = nextcord.Embed(  title="IQ",
                                    description=f"{ctx.author.mention} IQ-ja: **{random.randint(60, 230)}** IQ pont. Büszkék vagyunk rád.",
                                    color=0xe9b703,
                                    timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Radon × IQ", icon_url=ctx.author.display_avatar)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            try:
                member = await commands.MemberConverter().convert(ctx, member)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó! <:radon_x:811191514482212874>", color=0xFF9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Radon × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed)
                return
            embed = nextcord.Embed(title="IQ", description=f"{member.mention} IQ-ja: **{random.randint(60, 170)}** IQ pont. Büszkék vagyunk rád.", color=0xe9b703, timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed, mention_author=False)

        @commands.command(usage="love [1. felhasználó] [2. felhasználó]")
        async def love(self, ctx, member1, member2):
            try: member1 = await commands.MemberConverter().convert(ctx, member1); member2 = await commands.MemberConverter().convert(ctx, member2)
            except: 
                embed = nextcord.Embed(description="Nem található ilyen felhasználó!", color=0xFF9900, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f"Tyrion × Hiba", icon_url=ctx.author.display_avatar)
                await ctx.reply(embed=embed)
                return
            if member1 == member2: await ctx.reply("Aww, nyilván 100%, szeresd magad :)", mention_author=False);return
            embed = nextcord.Embed(description=f"{member1.mention} :grey_question: {member2.mention} [SZÁMOLÁS...]", color=0xe9b603, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Szeretet", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{member1.name} - {member2.name} × Kérte: {ctx.author.name}", icon_url=self.client.user.display_avatar)
            msg = await ctx.reply(embed=embed, mention_author=False)
            szam = random.randint(0, 100)
            if szam >= 90: emoji=":heart_on_fire:"
            if szam >=70 and szam< 90: emoji=":revolving_hearts:"
            if szam >=50 and szam<70: emoji=":heart:"
            if szam >=30 and szam<50: emoji=":broken_heart:"
            if szam >=0 and szam<30: emoji=":mending_heart:"
            await asyncio.sleep(random.randint(1, 4))
            embed = nextcord.Embed(description=f"{member1.mention} {emoji} {member2.mention} [**{szam}%**]")
            embed.set_author(name="Szeretet", icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"{member1.name} - {member2.name} × Kérte: {ctx.author.name}", icon_url=self.client.user.display_avatar)
            await msg.edit(embed=embed, content=None)

# információs parancsok

    @commands.command(aliases=["botinfo", "bot-info", "binfo", "bi", "boti"])
    async def botinfó(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = nextcord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        channelCount = len(set(self.bot.get_all_channels()))
        embed = nextcord.Embed(description="A Rebus bot információi", color=0xFF9900, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Bot neve", value="Rebus", inline=True)
        embed.add_field(name="Készült", value="2023.03.26", inline=True)
        embed.add_field(name="Programozási könytár", value="Nextcord")
        embed.add_field(name="Szerverek", value=f"{serverCount}")
        embed.add_field(name="Csatornák", value=f"{channelCount}")
        embed.add_field(name="Felhasználók", value=f"{memberCount}")
        embed.add_field(name="Python verzió", value=f"{pythonVersion}")
        embed.add_field(name="Parancsok száma", value=f"{len(self.bot.commands)}")
        embed.add_field(name="Operációs rendszer", value=f"Debian 10")
        embed.add_field(name="CPU kihasználtság", value=f"{psutil.cpu_percent()}%")
        embed.add_field(name="Memória kihasználtság", value=f"{psutil.virtual_memory().percent}%")
        embed.set_author(name="Bot információi", icon_url=ctx.author.display_avatar)
        embed.set_footer(text=f"{ctx.author.name} × Bot infók", icon_url=self.bot.user.display_avatar)
        await ctx.reply(embed=embed, mention_author=False)


    @commands.command(aliases=["ei", "einfo", "emojii", "emoteinfo"], usage=",emojiinfo [emoji (alap discordos emojit a bot nem fogad el)]")
    async def emojiinfo(self, ctx, emoji: nextcord.Emoji):
        try: emoji = await emoji.guild.fetch_emoji(emoji.id)
        except nextcord.NotFound: return await ctx.reply("Nem találtam ilyen emojit.", mention_author=False)
        is_managed = "Igen" if emoji.managed else "Nem"
        is_animated = "Igen" if emoji.animated else "Nem"
        embed=nextcord.Embed(color=0xFF9900, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Név", value=f"`{emoji.name}`")
        embed.add_field(name="ID", value=f"{emoji.id}")
        embed.add_field(name="Letöltés", value=f"**[Kattints ide!]({emoji.url})**")
        embed.add_field(name="Dátum", value=f"{emoji.created_at.strftime('%Y. %m. %d. @ %H:%M:%S')}")
        embed.add_field(name="Feltöltötte", value=f"{emoji.user.mention} (**{emoji.user}**)")
        embed.add_field(name="Formátum", value=f"`<:{emoji.name}:{emoji.id}>`")
        embed.add_field(name="Animált?", value=f"{is_animated}")
        embed.add_field(name="Kezelt?", value=f"{is_managed}")
        embed.set_author(name="Emojiinfo", icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"{ctx.author.name} × Emojiinfo", icon_url=self.bot.user.display_avatar)
        embed.set_thumbnail(url=emoji.url)
        await ctx.reply(embed=embed, mention_author=False)

        @commands.command()
        async def ping(ctx):
            await ctx.send(f"{self.bot.latency * 1000:.0f}ms")
# Tulajdonosi parancsok
        
@commands.command(usage=["eval [parancs]"])
async def eval(ctx, *, command):
    if ctx.message.author.id == 864583234158460938 or 1056315640048263230 or 452133888047972352:
        res = eval(command)
        if inspect.isawaitable(res):
            await ctx.send(await res)
    else:
        await ctx.send(res)

        @commands.command()
        async def serverlist(ctx):
            if ctx.author.id == 864583234158460938 or ctx.author.id == 1056315640048263230 or ctx.author.id == 452133888047972352:
                for guild in bot.guilds:
                    print(f"{guild.name} ({len(guild.members)})")
                    await ctx.message.delete()

def setup(bot):
    bot.add_cog(Commands(bot))