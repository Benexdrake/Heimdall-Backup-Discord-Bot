import discord

import os
from dotenv import load_dotenv

from cogs.buttons.accept import AcceptButton
from cogs.buttons.decline import DeclineButton

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
        load_dotenv()

        inviteChannel = interaction.client.get_guild(int(os.getenv('YGGDRASILID'))).get_channel(int(os.getenv('INVITE')))

        await interaction.response.send_message('Ok', ephemeral=True)

        q1 = os.getenv('q1') + ': \n```' + self.children[1].value+'```'
        q2 = os.getenv('q2') + ': \n```' + self.children[2].value+'```'
        q3 = os.getenv('q3') + ': \n```' + self.children[3].value+'```'

        await interaction.user.send(f'Anfrage wurde an die Admins gesendet.\n# Deine Antworten:\n{q1}\n{q2}\n{q3}\n')

        embed = discord.Embed(
            color=discord.Color.blue()
        )

        if 'https://twitter.com/' in self.children[0].value:
            embed.title='Twitter Profile'
            embed.url=self.children[0].value

        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar) 

        embed.add_field(name=os.getenv('q1'), value= q1, inline=False)
        embed.add_field(name=os.getenv('q2'), value= q2, inline=False)
        embed.add_field(name=os.getenv('q3'), value= q3, inline=False)
        
        thread = await inviteChannel.create_thread(name=interaction.user.mention,type=discord.ChannelType.public_thread)
        await thread.send(embed=embed)
        for value in self.values:
            accept = AcceptButton(id=str(interaction.user.id)+'_accept_'+value.replace(' ','_'), value=value)
            decline = DeclineButton(id=str(interaction.user.id)+'_decline_'+value.replace(' ','_'))
            view = discord.ui.View()
            view.add_item(accept)
            view.add_item(decline)
            await thread.send(content=value,view=view)

        

