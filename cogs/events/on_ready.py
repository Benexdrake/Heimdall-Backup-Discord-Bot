import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from logic.bifroest_logic import BifroestLogic
from logic.on_ready_logic import OnReadyLogic

class OnReady(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is Online')

        await BifroestLogic(self.bot).create()
        await OnReadyLogic(self.bot).insert_update_guilds_channels(self.bot.guilds)
        await OnReadyLogic(self.bot).sendServerInfos(self.bot.guilds)

def setup(bot:discord.Bot):
    bot.add_cog(OnReady(bot))