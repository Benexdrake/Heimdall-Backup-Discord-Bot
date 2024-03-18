import discord


async def create_channel(guild:discord.Guild,channelName:str):
    for channel in guild.channels:
        if channel.name == channelName:
            return
    await guild.create_text_channel(channelName)