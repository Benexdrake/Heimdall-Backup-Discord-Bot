import discord
from discord.ext import commands

from database.messages import Messages

class OnMessageDelete(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):
        Messages().delete(message.id)

def setup(bot:discord.Bot):
    bot.add_cog(OnMessageDelete(bot))