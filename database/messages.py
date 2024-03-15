import discord
from database.db_context import DbContext

class Messages:
    def insert(self,message:discord.Message):
        ctx = DbContext()
        q = f"""
            insert into messages values ({message.id}, {message.channel.id}, {False}, '{message.content}','{message.created_at}', {message.author.id});
            """
        ctx.execute(q);

    def update(self,message:discord.Message):
        ctx = DbContext()
        q = f"""
            update messages set message ='{message.content}' where id == {message.id};
            """
        ctx.execute(q);

    def delete(self, id):
        ctx = DbContext()
        q = f"""
            delete from messages where id == {id};
            """
        ctx.execute(q);
