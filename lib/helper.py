import os
import discord
from dotenv import load_dotenv, set_key

def update_env_channel_variable(channel, variable:str):
    dotenv_path = os.path.join(os.getcwd(), ".env")
    if channel.name == variable.lower():
        if os.getenv(variable):
            set_key(dotenv_path,key_to_set=variable, value_to_set=str(channel.id))

def update_env_variable(variable:str, value):
    
    dotenv_path = os.path.join(os.getcwd(), ".env")
    if variable in os.environ:
        set_key(dotenv_path,key_to_set=variable, value_to_set=str(value))

def create_env_variables():
        dotenv_path = os.path.join(os.getcwd(), ".env")

        if not os.path.exists(dotenv_path):
            with open(dotenv_path, "w") as f:
                print('Creating .env File for Configurations')
                f.write("")

        if os.getenv('BOTTOKEN') is None:
            with open(dotenv_path, "a") as f:
                print('ADDING BOTTOKEN into .env')
                f.write("BOTTOKEN='INSERT_TOKEN_HERE'\n")
        
        if os.getenv('DBNAME') is None:
            print('ADDING DBNAME into .env')
            with open(dotenv_path, "a") as f:
                f.write("DBNAME='helheim.db'\n")

        if os.getenv('FILESPATH') is None:
            print('ADDING FILESPATH into .env')
            with open(dotenv_path, "a") as f:
                f.write("FILESPATH='./FILES'\n")

async def purge(guild:discord.Guild, name:str):
    for channel in guild.channels:
        if channel.name == name:
            await channel.purge()

async def create_invite_link(guild:discord.Guild):
    for channel in guild.channels:
        if channel.type == discord.ChannelType.text:
            return await channel.create_invite(max_age=0, max_uses=0)
        
async def create_channel(guild:discord.Guild,channelName:str):
    for channel in guild.channels:
        if channel.name == channelName:
            return channel
    return await guild.create_text_channel(channelName)
                
async def info(bot:discord.Bot | discord.Client,info):
    for g in bot.guilds:
        if 'admin' in g.name.lower():
            logChannel = bot.get_channel(g.id)
            if logChannel:
                await logChannel.send(info)
            return
            
async def error(bot:discord.Bot | discord.Client, error):
    for g in bot.guilds:
        if 'admin' in g.name.lower():
            logChannel = bot.get_channel(g.id)
            if logChannel:
                await logChannel.send(f'Es ist ein Fehler aufgetreten ```{error}```')
            return
    