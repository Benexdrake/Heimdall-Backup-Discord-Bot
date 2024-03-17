import discord

from cogs.modals.questions import QuestionModal

options= [
    discord.SelectOption(label='Python', description='Python Beschreibung', emoji='😂'),
    discord.SelectOption(label='C#', description='C# Beschreibung', emoji='😍'),
    discord.SelectOption(label='Typescript', description='Typescript Beschreibung', emoji='🥰')
]

class InviteSelectView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.select_values = []

    @discord.ui.select(
    min_values=1,
    max_values=len(options),
    placeholder='Triff eine Auswahl',
    options=options,
    custom_id='dropdowntest123'
    )
    async def select_callback(self,select,interaction:discord.Interaction):
        self.select_values = select.values
        
        s=''
        for auswahl in select.values:
            s += f'- {auswahl}\n'

        await interaction.response.send_message(f'Du hast folgendes ausgewählt:\n{s}', ephemeral=True, view=InviteButtonView(select.values))
        
class InviteButtonView(discord.ui.View):
    def __init__(self, select_values):
        super().__init__(timeout=None)
        self.select_values = select_values

    @discord.ui.button(label='Click me for Invite', style=discord.ButtonStyle.primary, custom_id='invite_button', row=1)
    async def button_callback1(self,button,interaction:discord.Interaction):
        modal = QuestionModal(title='Invite Question Modal', values=self.select_values)
        await interaction.response.send_modal(modal)