import discord
from discord.ext import commands

from dotenv import load_dotenv
from lib.helper import error


class Error(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx:commands.Context,error):
        await error(self.bot,error)
        ctx.respond(f'You got an Error:\n{error}')
        raise error

def setup(bot):
    bot.add_cog(Error(bot))