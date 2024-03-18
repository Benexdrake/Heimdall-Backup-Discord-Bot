import discord
import os
from dotenv import load_dotenv

class Log:
    def __init__(self, bot:discord.Bot | discord.Client):
        load_dotenv()
        self.bot = bot

    async def info(self,info):
        if os.getenv('LOG') != ' ':
            logChannel = self.bot.get_channel(int(os.getenv('LOG')))
            if logChannel:
                await logChannel.send(info)

    async def error(self, error):
        if os.getenv('LOG'):
            logChannel = self.bot.get_channel(int(os.getenv('LOG')))
            if logChannel:
                await logChannel.send(f'Es ist ein Fehler aufgetreten ```{error}```')