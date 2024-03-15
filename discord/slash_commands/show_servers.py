import discord
from discord.ext import commands
from discord.commands import slash_command

import logic.show_servers_logic

#import os
#from dotenv import load_dotenv

class ShowServers(commands.cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions(administrator = True)
    @discord.guild_only()
    async def show_servers(self, ctx:commands.Context):
        await ctx.respond("Hallo Welt")
     

def setup(bot:discord.Bot):
    bot.add_cog(ShowServers(bot))