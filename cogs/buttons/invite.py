import discord

from cogs.modals.questions import ReactionModal

class InviteButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Click me for Invite', style=discord.ButtonStyle.primary, custom_id='invite_button', row=1)
    async def button_callback1(self,button,interaction:discord.Interaction):
        modal = ReactionModal(title='Invite Question Modal')
        await interaction.response.send_modal(modal)