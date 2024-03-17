import discord
from discord.ext import commands

from lib.inviteLink import InviteLink
from database.guilds import Guilds

class OnGuildJoin(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild:discord.Guild):
        g = await Guilds().get_by_id(guild.id)
        
        invite = await InviteLink().create(guild)
        
        if g == None:
            await Guilds().insert(guild, invite)
        else:
            await Guilds().update(guild,invite)

def setup(bot:discord.Bot):
    bot.add_cog(OnGuildJoin(bot))