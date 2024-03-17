import discord
import os
from dotenv import load_dotenv
from cogs.buttons.accept import AcceptButton
from cogs.buttons.decline import DeclineButton

class QuestionModalLogic:
    def __init__(self, interaction, values, children):
        self.interaction = interaction
        self.values = values
        self.children = children
        load_dotenv()

    async def callback(self):
        inviteChannel = self.interaction.client.get_guild(int(os.getenv('YGGDRASILID'))).get_channel(int(os.getenv('INVITE')))

        await self.interaction.response.send_message('Ok', ephemeral=True)

        q1 = os.getenv('q1') + ': \n```' + self.children[1].value+'```'
        q2 = os.getenv('q2') + ': \n```' + self.children[2].value+'```'
        q3 = os.getenv('q3') + ': \n```' + self.children[3].value+'```'

        await self.interaction.user.send(f'Anfrage wurde an die Admins gesendet.\n# Deine Antworten:\n{q1}\n{q2}\n{q3}\n')

        embed = discord.Embed(
            color=discord.Color.blue()
        )

        if 'https://twitter.com/' in self.children[0].value:
            embed.title='Twitter Profile'
            embed.url=self.children[0].value

        embed.set_author(name=self.interaction.user.display_name, icon_url=self.interaction.user.display_avatar) 

        embed.add_field(name=os.getenv('q1'), value= q1, inline=False)
        embed.add_field(name=os.getenv('q2'), value= q2, inline=False)
        embed.add_field(name=os.getenv('q3'), value= q3, inline=False)
        

        thread = await inviteChannel.create_thread(name=self.interaction.user.display_name,type=discord.ChannelType.public_thread)
        await thread.send(embed=embed)
        for value in self.values:
            accept = AcceptButton(id=str(self.interaction.user.id)+'_accept_'+value.replace(' ','_'), value=value)
            decline = DeclineButton(id=str(self.interaction.user.id)+'_decline_'+value.replace(' ','_'))
            view = discord.ui.View()
            view.add_item(accept)
            view.add_item(decline)
            await thread.send(content=value,view=view)
        await self.interaction.user.kick()
    