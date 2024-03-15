from database.db_context import DbContext

class TableGuild:
    def __init__(self):
        self.x = 1

    async def get(self,id):

        ctx = DbContext()
        result = ctx.execute(f"select * from Guilds where id == {id};")
        return result
    
    async def get_all(self):
        ctx = DbContext()
        result = ctx.execute(f'select * from Guilds')
        print(result)
        return result
    
    async def insert_update(self,id, name, invite):
        guild = await self.get(id=id)
        
        ctx = DbContext()
        q = ""
        if guild:
            q = f"""
                insert into guilds values ({id},'{name}','{invite}')
                """
        else:
            q = f"""
                update guilds set guildName = '{name}', inviteUrl = '{invite}' where id = {id}
                """
        ctx.execute(q)

    async def delete(self,id):
        ctx = DbContext()
        ctx.execute(f'delete from guilds where id == {id}')
