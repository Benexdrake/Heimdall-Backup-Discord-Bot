import discord

from database.guilds import Guilds


class ServerEmbed:
    async def create(self, guild:discord.Guild):
        g = await Guilds().get_by_id(guild.id)
        if len(g) == 0:
            return
        url = g[0][2]

        channelNames = []
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text:
                channelNames.append("- "+channel.name)

        description = "Owner: "+guild.owner.mention + "\n"+ "\n".join(channelNames)

        if guild.description:
            description += '\n' + f'```{guild.description}```'

        embed = discord.Embed(
            title=guild.name,
            description=description,
            color=discord.Color.blue()
        )

        embed.add_field(name='Users: ', value=str(guild.member_count), inline=True)
        embed.add_field(name='Channels: ', value=str(len(guild.channels)), inline=True)
        embed.add_field(name='Mods: ', value=f'{guild.owner.mention}\n{guild.owner.mention}\n{guild.owner.mention}\n{guild.owner.mention}\n{guild.owner.mention}\n', inline=False)
        
        if url != 'None':
            if guild.icon != None:
                embed.set_image(url=guild.icon.url)
                embed.set_author(name="Join Server", url=url, icon_url=guild.icon.url)
            else:
                embed.set_author(name="Join Server", url=url)
        
        embed.set_footer(text=guild.created_at)

        return embed