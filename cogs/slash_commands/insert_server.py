import discord
from discord.ext import commands
from discord.commands import slash_command

from logic.insert_server_logic import InsertServerLogic

#import os
#from dotenv import load_dotenv

class InsertServer(commands.Cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions(administrator = True)
    @discord.guild_only()
    async def insert_server(self, ctx:commands.Context):
        logic = InsertServerLogic()
        await logic.start(ctx)
       

def setup(bot:discord.Bot):
    bot.add_cog(InsertServer(bot))