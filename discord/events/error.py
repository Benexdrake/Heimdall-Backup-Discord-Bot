import discord
from discord.ext import commands

class Error(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx:commands.Context,error):
        channel = await self.bot.fetch_channel(1207776175225835530)
        ctx.respond(f'You got an Error: {error}')
        await channel.send(f'Es ist ein Fehler aufgetreten ```{error}```')
        raise error

def setup(bot):
    bot.add_cog(Error(bot))