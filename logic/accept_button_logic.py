import discord
from database.guilds import Guilds
from lib.helper import info

import os
from dotenv import load_dotenv

class AcceptButtonLogic:
    def __init__(self, interaction, custom_id, value):
        self.interaction = interaction
        self.custom_id = custom_id
        self.value = value
        load_dotenv()

    async def callback(self):
        idStr = str(self.custom_id)
        userId = int(idStr.split('_')[0])

        g = await Guilds().get_by_name(self.value)
        user = await self.interaction.client.fetch_user(int(userId))
        guild = self.interaction.client.get_guild(int(g[0][0]))

        for channel in guild.channels:
            if channel.name == os.getenv('INVITECHANNELNAME'):
                new_invite:discord.Invite = await channel.create_invite(max_uses=1)
                button = discord.ui.Button(label='Click for Invite',url=new_invite.url)
                view = discord.ui.View()
                view.add_item(button)
                await user.send('You got Accepted',view=view)
                message = await self.interaction.response.send_message('Accept')
                await message.delete_original_response()
                await self.interaction.message.delete()
                await info(self.interaction.client,f'User {self.interaction.user.mention} got Accepted for Server {self.value}')
                return