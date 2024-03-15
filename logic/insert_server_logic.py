import discord
from discord.ext import commands

from database.table_guilds import TableGuild

import os
from dotenv import load_dotenv

class InsertServerLogic():
    def __init__(self):
        load_dotenv()

    async def start(self,ctx:commands.Context):
        guildId = ctx.guild.id
        guildName = ctx.guild.name
        inviteLink = ""

        for channel in ctx.guild.channels:
            if channel.type == discord.ChannelType.text:
                inviteLink = await channel.create_invite(max_age=0, max_uses=0)
                break
        if inviteLink != "":
            tg = TableGuild()
            await tg.insert_update(id=guildId, name=guildName, invite=inviteLink)
        await ctx.respond("Hi")