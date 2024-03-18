import discord
from discord.ext import commands
from dotenv import load_dotenv
from logic.on_ready_logic import OnReadyLogic

class OnReady(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_ready(self):
        await OnReadyLogic(self.bot).start()

def setup(bot:discord.Bot):
    bot.add_cog(OnReady(bot))