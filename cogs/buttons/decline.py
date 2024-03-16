import discord

from cogs.modals.decline import DeclineModal

class DeclineButton(discord.ui.Button):
    def __init__(self,id):
        super().__init__(label='Decline', style=discord.ButtonStyle.danger, custom_id=str(id), row=1)

    async def button_decline_callback2(self,interaction:discord.Interaction):
        userId = self.custom_id
        modal = DeclineModal(title=userId)
        await interaction.response.send_modal(modal)