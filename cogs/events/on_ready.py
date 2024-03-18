import discord
from discord.ext import commands
import os
from dotenv import load_dotenv,dotenv_values, set_key
from lib.create_channel import create_channel
from logic.bifroest_logic import BifroestLogic
from logic.on_ready_logic import OnReadyLogic

from lib.purgeChannel import purge

class OnReady(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is Online')

        
        dotenv_path = os.path.join(os.getcwd(), ".env")

        for guild in self.bot.guilds:
            if not os.getenv('YGGDRASILID'):
                if guild.description:
                    if 'admin' in guild.description:
                        with open(dotenv_path, "a") as f:
                            f.write(f"YGGDRASILID={guild.id}\n")
            else:
                if guild.id == int(os.getenv('YGGDRASILID')):
                        await create_channel(guild,'log')
                        await create_channel(guild,'invite')
                        await purge(guild,'LOG')
                        await purge(guild,'INVITE')
                        
        


            
        
        newChannel = await BifroestLogic(self.bot).create()
        await OnReadyLogic(self.bot).insert_update_guilds_channels(self.bot.guilds)
        await BifroestLogic(self.bot).send(newChannel)
        await OnReadyLogic(self.bot).sendServerInfos(self.bot.guilds)

def setup(bot:discord.Bot):
    bot.add_cog(OnReady(bot))