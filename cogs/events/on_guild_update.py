import discord
from discord.ext import commands

from database.guilds import Guilds
from lib.helper import create_invite_link

class OnGuildUpdate(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self,before,after):
        invite = await create_invite_link(after)
        await Guilds().update(after,invite)
        
def setup(bot:discord.Bot):
    bot.add_cog(OnGuildUpdate(bot))