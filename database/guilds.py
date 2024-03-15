from database.db_context import DbContext

class Guilds:    
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
            update guilds set guildName = '{guild.name}', inviteUrl= '{invite}' where id = {guild.id};
            """
        ctx.execute(q)