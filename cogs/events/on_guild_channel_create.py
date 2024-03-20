import discord
from discord.ext import commands

from database.channels import Channels
from lib.helper import update_env_channel_variable
from lib.helper import info
import os
from dotenv import load_dotenv


class OnChannelCreate(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel:discord.TextChannel):
        # if 'admin' in channel.guild.name.lower():
        #     update_env_channel_variable(channel,'LOG')
        #     update_env_channel_variable(channel,'INVITE')

        await Channels().insert(channel)
        await info(self.bot,f'Created: {channel.name} in {channel.guild.name}')

def setup(bot:discord.Bot):
    bot.add_cog(OnChannelCreate(bot))