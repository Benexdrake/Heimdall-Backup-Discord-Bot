import discord
from discord.ext import commands

from database.messages import Messages

class OnMessageEdit(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        await Messages().update(after)
        

def setup(bot:discord.Bot):
    bot.add_cog(OnMessageEdit(bot))