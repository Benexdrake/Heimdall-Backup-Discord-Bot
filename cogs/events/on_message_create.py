import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
import requests

from database.messages import Messages
from logic.on_message_logic import OnMessageLogic

class OnMessage(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
     

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        await OnMessageLogic().create(message)
        

def setup(bot:discord.Bot):
    bot.add_cog(OnMessage(bot))