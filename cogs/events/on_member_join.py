import discord
from discord.ext import commands

from lib.helper import info

class OnMemberJoin(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member:discord.Member):
        await info(self.bot,f"{member.mention} joined {member.guild.name}")

def setup(bot:discord.Bot):
    bot.add_cog(OnMemberJoin(bot))