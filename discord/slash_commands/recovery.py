import discord
from discord.ext import commands
from discord.commands import slash_command

import logic.recovery_logic

#import os
#from dotenv import load_dotenv

class Recovery(commands.cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions(administrator = True)
    @discord.guild_only()
    async def recovery(self, ctx:commands.Context):
        await ctx.respond("Hallo Welt")
        

def setup(bot:discord.Bot):
    bot.add_cog(Recovery(bot))