import discord
from discord.ext import commands
from discord.commands import slash_command

import logic.bifroest_logic
#import os
#from dotenv import load_dotenv

class CreateBifroest(commands.cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions(administrator = True)
    @discord.guild_only()
    async def create_bifroest(self, ctx:commands.Context):
        await ctx.respond("Hallo Welt")
        # Abfrage Datenbank ob ein Bifröst Server schon existiert
        # Überprüfen ob Bot auf Bifröst ist
        # Ist der Bot nicht auf Biföst, so wird die in der DB gespeicherte überschrieben und ein neuer Server wird erstellt.
        # Erstellt auf dem neuen Server den Text Channel Midgard und löscht alle anderen.
        # Ändert Midgard auf Readonly
        # Fügt Text für Regeln in Midgard
        # Fragt die DB nach einer Liste von Servern die nicht Bifröst oder Yggdrasil sind ab und erstellt ein Dropdownlist
        # Fügt einen Invite Request Button hinzu

def setup(bot:discord.Bot):
    bot.add_cog(CreateBifroest(bot))