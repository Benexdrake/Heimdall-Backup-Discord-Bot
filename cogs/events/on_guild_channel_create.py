import discord
from discord.ext import commands

from database.channels import Channels
from lib.log import Log
import os
from dotenv import load_dotenv,dotenv_values, set_key


class OnChannelCreate(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel:discord.TextChannel):

        dotenv_path = os.path.join(os.getcwd(), ".env")
        if os.getenv('YGGDRASILID'):
            if channel.guild.id == int(os.getenv('YGGDRASILID')):
                if channel.name == 'log':
                    if os.getenv('LOG'):
                        set_key(dotenv_path,key_to_set='LOG', value_to_set=str(channel.id))
                if channel.name == 'invite':
                    if os.getenv('INVITE'):
                        set_key(dotenv_path,key_to_set='INVITE', value_to_set=str(channel.id))

        await Channels().insert(channel)
        await Log(self.bot).info(f'Created: {channel.name} in {channel.guild.name}')

def setup(bot:discord.Bot):
    bot.add_cog(OnChannelCreate(bot))