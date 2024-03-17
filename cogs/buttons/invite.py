import discord

from cogs.modals.questions import QuestionModal




class InviteSelect(discord.ui.Select):
    def __init__(self, custom_id, placeholder, max_values, options):
        super().__init__(custom_id=custom_id, placeholder=placeholder, min_values=1, max_values=max_values, options=options)
        self.select_values = []

    async def callback(self, interaction: discord.Interaction):
        self.select_values = self.values
        
        s=''
        for auswahl in self.values:
            s += f'- {auswahl}\n'
        await interaction.response.send_message(f'Du hast folgendes ausgewählt:\n{s}', ephemeral=True, view=InviteButtonView(self.values))
        
class InviteButtonView(discord.ui.View):
    def __init__(self, select_values):
        super().__init__(timeout=None)
        self.select_values = select_values

    @discord.ui.button(label='Click me for Invite', style=discord.ButtonStyle.primary, custom_id='invite_button', row=1)
    async def callback(self,button,interaction:discord.Interaction):
        modal = QuestionModal(title='Invite Question Modal', values=self.select_values)
        await interaction.response.send_modal(modal)