import discord
from discord.ext import commands
from discord.commands import slash_command

from logic.show_servers_logic import ShowServersLogic

#import os
#from dotenv import load_dotenv

class ShowServers(commands.Cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions(administrator = True)
    @discord.guild_only()
    async def show_servers(self, ctx:commands.Context):
        logic = ShowServersLogic()
        await logic.start(ctx)
     

def setup(bot:discord.Bot):
    bot.add_cog(ShowServers(bot))