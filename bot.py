import discord
import os
from dotenv import load_dotenv

class Bot(discord.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        status = discord.Status.dnd
        activity = discord.Activity(type=discord.ActivityType.watching, name='von Asgard runter')

        super().__init__(intents=intents, debug_guilds=[998136328032112671], status=status, activity=activity)

    def run(self):
        self.loading('events')
        self.loading('slash_commands')

        load_dotenv()
        super().run(os.getenv('BOTTOKEN'))

    def loading(self,folder:str):
        for filename in os.listdir(f"discord/{folder}"):
            if filename.endswith('.py'):
                print(f'Loading {folder}: {filename[:-3]}')
                super().load_extension(f'{folder}.{filename[:-3]}')
