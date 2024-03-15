from database.db_context import DbContext

class Channels:
    async def get(self, id):
        ctx = DbContext()
        q = f"""
                select * from channels where id = {id};
            """
        return ctx.execute(q);

    async def insert(self,channel):
        ctx = DbContext()
        q = f"""
                insert into channels values ({channel.id},{channel.guild.id},'{channel.name}',true);
            """
        ctx.execute(q);

    async def update(self,id, hasBackup):
        ctx = DbContext()
        q = f"""
            update channels set hasBackup = {hasBackup} where id == {id};
            """
        ctx.execute(q);