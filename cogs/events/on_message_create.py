import discord
from discord.ext import commands

from database.messages import Messages

class OnMessage(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        if(message.author.bot or message.author.system):
            return
        Messages().insert(message)
        

def setup(bot:discord.Bot):
    bot.add_cog(OnMessage(bot))