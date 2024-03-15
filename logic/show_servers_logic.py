import discord
from discord.ext import commands

from database.table_guilds import TableGuild

class ShowServersLogic():
    #def __init__(self):

    async def start(self, ctx:commands.Context):
        tg = TableGuild()
        guilds = await tg.get_all()
        

        if guilds:
            await ctx.respond(f'{len(guilds)} Guilds in DB')
        else:
            await ctx.respond('No Guilds in DB')
        