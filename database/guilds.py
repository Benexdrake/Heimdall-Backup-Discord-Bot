from database.db_context import DbContext

class Guilds:
    async def get(self,id):
        ctx = DbContext()
        result = ctx.execute(f"select * from Guilds where id == {id};")
        return result
    
    async def get_all(self):
        ctx = DbContext()
        result = ctx.execute(f'SELECT * FROM Guilds;')
        return result
    
    async def insert(self,guild, invite):
        ctx = DbContext()
        q = f"""
            insert into guilds values ({guild.id},'{guild.name}','{invite}');
            """
        ctx.execute(q)

    async def update(self, guild, invite):
        ctx = DbContext()
        q = f"""
            update guilds set name = '{guild.name}', inviteUrl= '{invite}' where id = {guild.id};
            """
        ctx.execute(q)