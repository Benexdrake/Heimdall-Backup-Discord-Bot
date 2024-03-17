import discord

from logic.decline_button_logic import DeclineButtonLogic

class DeclineButton(discord.ui.Button):
    def __init__(self,id):
        super().__init__(label='Decline', style=discord.ButtonStyle.danger, custom_id=str(id), row=1)

    async def button_decline_callback2(self,interaction:discord.Interaction):
        await DeclineButtonLogic(interaction, self.custom_id).callback()