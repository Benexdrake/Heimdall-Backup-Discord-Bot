import discord
from discord.ext import commands

class BifroestLogic():
    #def __init__(self):

    async def start(self, ctx:commands.Context):
        await ctx.respond(self.__class__.__name__)