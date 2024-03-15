import discord
from discord.ext import commands

from logic.insert_server_logic import InsertServerLogic

class OnGuildJoin(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild:discord.Guild):
        # send Guild ID, Name and create a invite Link into db
        logic = InsertServerLogic()
        await logic.start(guild)
        

def setup(bot:discord.Bot):
    bot.add_cog(OnGuildJoin(bot))