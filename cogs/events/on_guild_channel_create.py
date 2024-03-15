import discord
from discord.ext import commands

from database.channels import Channels

class OnChannelCreate(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel:discord.TextChannel):
        await Channels().insert(channel)

def setup(bot:discord.Bot):
    bot.add_cog(OnChannelCreate(bot))