import discord

from cogs.embeds.server_embed import ServerEmbed
from database.channels import Channels
from database.guilds import Guilds
from lib.inviteLink import InviteLink

class OnMessageCreate:
    async def insert_update_guilds_channels(self, guilds):
        for guild in guilds:
            guildsDb = await Guilds().get(guild.id)
            if len(guildsDb) == 0:
                invite = await InviteLink().create(guild)
                await Guilds().insert(guild,invite)
            else:
                invite = await InviteLink().create(guild)
                await Guilds().update(guild,invite)

            for channel in guild.channels:
                if channel.type == discord.ChannelType.text:
                    channelsDb = await Channels().get(channel.id)
                    if len(channelsDb) == 0:
                        await Channels().insert(channel)
                    else:
                        await Channels().update(channel)

    async def getServerList(self, guild):
        channelId = ''
        for channel in guild.channels:
            if channel.name == 'server-list':
                channelId = channel.id
                await channel.purge()
                break
        if channelId == '':
            c = await guild.create_text_channel('server-list')
            channelId = c.id
        return channelId
    
    async def sendServerInfos(self,guilds,guild, channelId):
        for g in guilds:
            embed = await ServerEmbed().create(g)
            getChannel = guild.get_channel(channelId)
            await getChannel.send(embed=embed)