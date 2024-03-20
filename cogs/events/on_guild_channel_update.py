import discord
from discord.ext import commands

from database.channels import Channels
from lib.helper import info


class OnChannelUpdate(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_update(self,before:discord.TextChannel, after:discord.TextChannel):
        if after.type == discord.ChannelType.text:
            await Channels().update(after)
            await info(self.bot,f'Updated: {after.name} in {after.guild.name}')

def setup(bot:discord.Bot):
    bot.add_cog(OnChannelUpdate(bot))