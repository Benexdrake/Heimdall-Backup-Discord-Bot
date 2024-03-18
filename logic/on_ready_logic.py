
import discord
import os
from dotenv import load_dotenv
from cogs.embeds.server_embed import ServerEmbed
from database.channels import Channels
from database.guilds import Guilds
from lib.helper import create_channel
from lib.helper import create_invite_link, purge
from logic.bifroest_logic import BifroestLogic

class OnReadyLogic:
    def __init__(self, bot:discord.Bot):
        load_dotenv()
        self.bot = bot

    async def start(self):
        print(f'{self.bot.user.name} is Online')
        dotenv_path = os.path.join(os.getcwd(), ".env")
        for guild in self.bot.guilds:
            if not os.getenv('YGGDRASILID'):
                if guild.description:
                    if 'admin' in guild.description:
                        with open(dotenv_path, "a") as f:
                            f.write(f"YGGDRASILID={guild.id}\n")
            else:
                if guild.id == int(os.getenv('YGGDRASILID')):
                        await create_channel(guild,'log')
                        await create_channel(guild,'invite')
                        await purge(guild,'log')
                        await purge(guild,'invite')
            
        newChannel = await BifroestLogic(self.bot).create()
        await self.insert_update_guilds_channels(self.bot.guilds)
        await BifroestLogic(self.bot).send(newChannel)
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
        guild = self.bot.get_guild(int(os.getenv('YGGDRASILID')))
        await purge(guild,'server-list')
        return await create_channel(guild,'server-list')
    
    async def sendServerInfos(self):
        channel = await self.getServerList()
        if channel:
            for guild in self.bot.guilds:

                embed = await ServerEmbed().create(guild)
                await channel.send(embed=embed)