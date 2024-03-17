import discord
import json

from database.db_context import DbContext



class Messages:
    async def insert(self,message:discord.Message):
        hasFiles = False

        if len(message.attachments) > 0:
            hasFiles = True

        ignore_list = []
        with open("serverIgnoreList.json", "r") as f:
            data = json.load(f)
            ignore_list = data["Ignore"]

        if message.channel.name in ignore_list:
            return

        ctx = DbContext()
        q = f"""
            insert into messages values ({message.id}, {message.channel.id}, {hasFiles}, '{message.content}','{message.created_at}', {message.author.id});
            """
        ctx.execute(q);

    async def update(self,message:discord.Message):
        ctx = DbContext()
        q = f"""
            update messages set message ='{message.content}' where id == {message.id};
            """
        ctx.execute(q);

    async def delete(self, id):
        ctx = DbContext()
        q = f"""
            delete from messages where id == {id};
            """
        ctx.execute(q);
