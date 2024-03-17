import discord
from logic.question_modal_logic import QuestionModalLogic
import os

class QuestionModal(discord.ui.Modal):
    def __init__(self, values,*args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label='Code aus pn',
                placeholder='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                style=discord.InputTextStyle.singleline, 
                required=True
            ),
            discord.ui.InputText(
                label='Frage 1:',
                placeholder=os.getenv('q1'),
                style=discord.InputTextStyle.long, 
                required=True
            ),
            discord.ui.InputText(
                label='Frage 2:',
                placeholder=os.getenv('q2'),
                style=discord.InputTextStyle.long, 
                required=True
            ),
            discord.ui.InputText(
                label='Frage 3:',
                placeholder=os.getenv('q3'),
                style=discord.InputTextStyle.long, 
                required=True
            ),
            *args,
            **kwargs)
        self.values = values
        
    async def callback(self, interaction: discord.Interaction):
        await QuestionModalLogic(interaction, self.values, self.children).callback()

        

