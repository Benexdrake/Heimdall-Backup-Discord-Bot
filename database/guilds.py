import discord
from database.db_context import DbContext

class Guilds:
    def __init__(self):
        pass

    async def get_by_id(self,id):
        ctx = DbContext()
        result = ctx.execute(f"select * from Guilds where id == {id};")
        return result
    
    async def get_by_name(self,name):
        ctx = DbContext()
        result = ctx.execute(f"select * from Guilds where name = '{name}';")
        return result
    
    async def get_all(self):
        ctx = DbContext()
        result = ctx.execute(f'SELECT * FROM Guilds;')
        return result
    
    async def insert(self,guild:discord.Guild, invite):
        ctx = DbContext()
        description = None
        if guild.description:
            description = guild.description
        q = f"""
            insert into guilds values ({guild.id},'{guild.name}','{invite}', '{description}');
            """
        ctx.execute(q)

    async def update(self, guild, invite):
        ctx = DbContext()
        description = None
        if guild.description:
            description = guild.description
        q = f"""
            update guilds set name = '{guild.name}', inviteUrl= '{invite}', description = '{description}' where id = {guild.id};
            """
        ctx.execute(q)
    
    async def delete(self, name):
        ctx = DbContext()
        q = f"""
            delete from guilds where name = '{name}';
            """
        ctx.execute(q)
