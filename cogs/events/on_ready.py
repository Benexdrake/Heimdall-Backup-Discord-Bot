import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from logic.on_ready_logic import OnMessageCreate
from cogs.embeds.server_embed import ServerEmbed

class OnReady(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        load_dotenv()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is Online')

        await OnMessageCreate().insert_update_guilds_channels(self.bot.guilds)

        guild = self.bot.get_guild(int(os.getenv('YGGDRASILID')))

        channelId = await OnMessageCreate().getServerList(guild)

        await OnMessageCreate().sendServerInfos(self.bot.guilds,guild,channelId)


def setup(bot:discord.Bot):
    bot.add_cog(OnReady(bot))