import discord
class InviteLink:
    async def create(self,guild:discord.Guild):
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text:
                return await channel.create_invite(max_age=0, max_uses=0)
                
        
        