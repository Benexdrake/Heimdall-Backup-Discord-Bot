import discord
from discord.ext import commands

from database.channels import Channels
from lib.helper import info



class OnChannelDelete(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel:discord.TextChannel):
        await Channels().delete(channel)
        await info(self.bot,f'Deleted: {channel.name} from {channel.guild.name}')

def setup(bot:discord.Bot):
    bot.add_cog(OnChannelDelete(bot))