import discord

from lib.log import Log

import os
from dotenv import load_dotenv

class AcceptButton(discord.ui.Button):
    def __init__(self, id):
        super().__init__(label='Accept', style=discord.ButtonStyle.green, row=1, custom_id=id)
        load_dotenv()
        

    async def callback(self,interaction:discord.Interaction):
        userId = int(self.custom_id)

        user = await interaction.client.fetch_user(int(userId))

        guild:discord.Guild = interaction.client.get_guild(int(os.getenv('secretGuild')))
        
        channel:discord.TextChannel = guild.get_channel(int(os.getenv('secretGuildChannel')));
        new_invite:discord.Invite = await channel.create_invite(max_uses=1)

        button = discord.ui.Button(label='Discord Invite Link',url=new_invite.url)
        view = discord.ui.View()
        view.add_item(button)
        
        await user.send('You got Accepted')
        
        message = await interaction.response.send_message('Accept', view=view)

        await message.delete_original_response()
        await interaction.message.delete()

        await Log(interaction.client).info(f'User {interaction.user.mention} got Accepted for Server X')
        