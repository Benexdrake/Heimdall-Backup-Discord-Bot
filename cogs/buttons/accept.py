import discord
from logic.accept_button_logic import AcceptButtonLogic

class AcceptButton(discord.ui.Button):
    def __init__(self, id, value):
        super().__init__(label='Accept', style=discord.ButtonStyle.green, row=1, custom_id=id)
        self.value = value
        

    async def callback(self,interaction:discord.Interaction):
        await AcceptButtonLogic(interaction, self.custom_id, self.value).callback()
        