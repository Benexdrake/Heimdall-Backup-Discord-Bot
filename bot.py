import discord
import os
from dotenv import load_dotenv

from database.db_context import DbContext

class Bot(discord.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        intents.guilds = True
        intents.members = True
        status = discord.Status.dnd
        activity = discord.Activity(type=discord.ActivityType.watching, name='von Asgard aus runter')

        super().__init__(intents=intents,debug_guilds=[1214965274562928751] ,status=status, activity=activity)

    def run(self):
        db = DbContext()
        db.load_database()

        self.loading('events')
        self.loading('slash_commands')

        load_dotenv()
        super().run(os.getenv('BOTTOKEN'))

    def loading(self,folder:str):
        for filename in os.listdir(f"cogs\{folder}"):
            if filename.endswith('.py'):
                print(f'Loading {folder}: {filename[:-3]}')
                super().load_extension(f'cogs.{folder}.{filename[:-3]}')
