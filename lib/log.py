import discord
import os
from dotenv import load_dotenv

class Log:
    def __init__(self, bot:discord.Bot):
        load_dotenv()
        self.bot = bot

    async def info(self,info):
        logChannel = await self.bot.fetch_channel(int(os.getenv('LOG')))
        await logChannel.send(info)

    async def error(self, error):
        logChannel = await self.bot.fetch_channel(int(os.getenv('LOG')))
        await logChannel.send(f'Es ist ein Fehler aufgetreten ```{error}```')