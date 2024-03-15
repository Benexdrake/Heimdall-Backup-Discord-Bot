import discord
from discord.ext import commands

from database.channels import Channels
from database.guilds import Guilds
from lib.inviteLink import InviteLink

class OnReady(commands.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is Online')
        for guild in self.bot.guilds:
            g = await Guilds().get(guild.id)
            if len(g) == 0:
                invite = await InviteLink().create(guild)
                await Guilds().insert(guild,invite)
            else:
                t = g[0]
                await Guilds().update(guild,t[2])

            for channel in guild.channels:
                if channel.type == discord.ChannelType.text:
                    c = await Channels().get(channel.id)
                    if len(c) == 0:
                        await Channels().insert(channel)
                    else:
                        ct = c[0]
                        await Channels().update(channel.id, ct[3])


def setup(bot:discord.Bot):
    bot.add_cog(OnReady(bot))