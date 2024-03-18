import os
import discord
from discord import PermissionOverwrite, Role, Member

from cogs.buttons.invite import InviteSelect
from database.guilds import Guilds

from dotenv import load_dotenv


class BifroestLogic():
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    async def create(self):
        guilds = self.bot.guilds

        for guild in guilds:
            if "Midgard" in guild.name:
                await guild.delete()
                await Guilds().delete(name='Midgard')

        with open("Tor.png", "rb") as f:
            icon_bytes = f.read()

        newGuild = await self.bot.create_guild(name='Midgard',icon=icon_bytes)
        g = self.bot.get_guild(newGuild.id)
        overwrite = PermissionOverwrite(view_channel=False)
        for c in g.channels:
            await c.set_permissions(c.guild.default_role,overwrite=overwrite)    
        newChannel = await newGuild.create_text_channel(name='idavoll')
        perms = newChannel.overwrites_for(newChannel.guild.default_role)
        perms.send_messages = False
        await newChannel.set_permissions(newChannel.guild.default_role, overwrite=perms)
        invite = await newChannel.create_invite()
        await Guilds().update(guild,invite.url)
        return newChannel

        

    async def send(self,newChannel:discord.TextChannel):
        guilds = await Guilds().get_all()

        options = []

        for g in guilds:
            if 'admin' in g[1].lower() or newChannel.guild.name.lower() in g[1].lower():
                continue
            options.append(discord.SelectOption(label=g[1], description='-'))
        
        view = discord.ui.View()
        select = InviteSelect(custom_id='select_servers',placeholder='Select Server',max_values=len(options),options=options)
        view.add_item(select)

        await newChannel.send('Regeln',view=view)