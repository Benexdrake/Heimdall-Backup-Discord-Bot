import discord
from logic.question_modal_logic import QuestionModalLogic
import os

class QuestionModal(discord.ui.Modal):
    def __init__(self, values,*args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label='Twitter Account Url',
                placeholder='https://twitter.com/your_username',
                style=discord.InputTextStyle.singleline, 
                required=False
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

        

