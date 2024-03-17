from cogs.modals.decline import DeclineModal

class DeclineButtonLogic:
    def __init__(self, interaction, custom_id):
        self.interaction=interaction
        self.custom_id = custom_id
        

    async def callback(self):
        idStr = str(self.custom_id)
        userId = int(idStr.split('_')[0])

        modal = DeclineModal(title=userId)
        
        await self.interaction.response.send_modal(modal)