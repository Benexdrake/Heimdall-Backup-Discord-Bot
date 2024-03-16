import discord
import json

from database.guilds import Guilds


class ServerEmbed:
    async def create(self, guild:discord.Guild):
        g = await Guilds().get(guild.id)
        if len(g) == 0:
            return
        url = g[0][2]

        channelNames = []
        for channel in guild.channels:
            if channel.type == discord.ChannelType.text:
                channelNames.append("- "+channel.name)

        description = "Owner: "+guild.owner.mention + "\n"+ "\n".join(channelNames)

        embed = discord.Embed(
            title=guild.name,
            description=description,
            color=discord.Color.blue()
        )

        embed.set_author(name="Click for join Server", url=url, icon_url=guild.icon.url)

        embed.set_footer(text=guild.created_at)

        return embed

        

        
        