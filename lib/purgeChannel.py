import os
import discord

async def purge(guild:discord.Guild, envName:str):
    if os.getenv(envName) != ' ':
        channel = guild.get_channel(int(os.getenv(envName)))
        if channel:
            await channel.purge()