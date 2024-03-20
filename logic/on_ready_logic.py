
import discord
import os
from dotenv import load_dotenv
from cogs.embeds.server_embed import ServerEmbed
from database.channels import Channels
from database.guilds import Guilds
from lib.helper import create_channel
from lib.helper import create_invite_link, purge, update_env_variable

class OnReadyLogic:
    def __init__(self, bot:discord.Bot):
        load_dotenv()
        self.bot = bot

    async def start(self):
        print(f'{self.bot.user.name} is Online')

        for guild in self.bot.guilds:
                if 'admin' in guild.name.lower():
                    c1 = await create_channel(guild,'log')
                    update_env_variable('LOG', c1.id)
                    c2 = await create_channel(guild,'invite')
                    update_env_variable('INVITE', c2.id)
                    await purge(guild,'log')
                    await purge(guild,'invite')
                        
        load_dotenv()
        await self.sendServerInfos()

    async def insert_update_guilds_channels(self, guilds):
        for guild in guilds:
            guildsDb = await Guilds().get_by_id(guild.id)
            invite = await create_invite_link(guild)
            if len(guildsDb) == 0:
                await Guilds().insert(guild,invite)
            else:
                await Guilds().update(guild,invite)

            for channel in guild.channels:
                if channel.type == discord.ChannelType.text:
                    channelsDb = await Channels().get(channel.id)
                    if len(channelsDb) == 0:
                        await Channels().insert(channel)
                    else:
                        await Channels().update(channel)

    async def getServerList(self):
        for guild in self.bot.guilds:
            if 'admin' in guild.name.lower():
                await purge(guild,'server-list')
                return await create_channel(guild,'server-list')
    
    async def sendServerInfos(self):
        load_dotenv()
        channel = await self.getServerList()
        if channel:
            for guild in self.bot.guilds:

                embed = await ServerEmbed().create(guild)
                await channel.send(embed=embed)