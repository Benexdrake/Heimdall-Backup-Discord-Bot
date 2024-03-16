import discord
from discord import PermissionOverwrite, Role, Member

from cogs.buttons.invite import InviteButtonView
from database.guilds import Guilds



class BifroestLogic():
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        pass

    async def create(self):
        guilds = self.bot.guilds

        for guild in guilds:
            if "Midgard" in guild.name:
                await guild.delete()
                await Guilds().delete(name='Midgard')
        
        newGuild = await self.bot.create_guild(name='Midgard')
        g = self.bot.get_guild(newGuild.id)
        overwrite = PermissionOverwrite(view_channel=False)
        for c in g.channels:
            await c.set_permissions(c.guild.default_role,overwrite=overwrite)    
        newChannel = await newGuild.create_text_channel(name='Idavall')
        perms = newChannel.overwrites_for(newChannel.guild.default_role)
        perms.send_messages = False
        await newChannel.set_permissions(newChannel.guild.default_role, overwrite=perms)
        invite = await newChannel.create_invite()
        await Guilds().update(guild,invite.url)
        
        await newChannel.send('Regeln',view=InviteButtonView())