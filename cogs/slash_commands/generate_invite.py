import discord
from discord.ext import commands
from discord.commands import slash_command

import uuid

from database.guids import Guids

class GenerateInvite(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
    @slash_command()
    async def generate_invite(self,ctx:commands.Context):
        inviteUrl = None
        for guild in self.bot.guilds:
            if guild.name == 'Midgard':
                for channel in guild.channels:
                    if channel.name == 'idavoll':
                        inviteUrl = await channel.create_invite(max_uses=1)

        if inviteUrl != None:
            guid = uuid.uuid4()
            await Guids().insert(str(guid))
            await ctx.respond(f'```Bitte ID angeben:\n{guid}\nInvite Link:\n{inviteUrl.url}```',ephemeral=True)
            return
        await ctx.respond('Error',ephemeral=True)


def setup(bot:discord.Bot):
    bot.add_cog(GenerateInvite(bot))