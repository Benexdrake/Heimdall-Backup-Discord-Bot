import discord

from database.guilds import Guilds
from lib.log import Log

import os
from dotenv import load_dotenv

class AcceptButton(discord.ui.Button):
    def __init__(self, id, value):
        super().__init__(label='Accept', style=discord.ButtonStyle.green, row=1, custom_id=id)
        load_dotenv()
        self.value = value
        

    async def callback(self,interaction:discord.Interaction):
        idStr = str(self.custom_id)
        userId = int(idStr.split('_')[0])

        g = await Guilds().get_by_name(self.value)
        user = await interaction.client.fetch_user(int(userId))
        guild = interaction.client.get_guild(int(g[0][0]))

        for channel in guild.channels:
            if channel.name == os.getenv('INVITECHANNELNAME'):
                new_invite:discord.Invite = await channel.create_invite(max_uses=1)
                button = discord.ui.Button(label='Click for Invite',url=new_invite.url)
                view = discord.ui.View()
                view.add_item(button)
                await user.send('You got Accepted',view=view)
                message = await interaction.response.send_message('Accept')
                await message.delete_original_response()
                await interaction.message.delete()
                await Log(interaction.client).info(f'User {interaction.user.mention} got Accepted for Server {self.value}')
                return
        