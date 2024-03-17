import discord

class DeclineModal(discord.ui.Modal):
    def __init__(self, userId,*args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label='Begründung:',
                placeholder='Begründung eingeben',
                style=discord.InputTextStyle.long, 
                required=True
            ),
            *args,
            **kwargs)
        self.userId = userId
        
    async def callback(self, interaction: discord.Interaction):
        message = await interaction.response.send_message('OK')
        await interaction.message.delete()
        await message.delete_original_response()
        user = await interaction.client.fetch_user(int(self.userId))
        await user.send(f'# Begründung:\n{self.children[0].value}')