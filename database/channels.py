from database.db_context import DbContext

class Channels:
    def insert(self,id,guildId):
        ctx = DbContext()
        q = f"""
                insert into channels values ({id},{guildId},true);
            """
        ctx.execute(q);

    def update(self,id, hasBackup):
        ctx = DbContext()
        q = f"""
            update channels set hasBackup = {hasBackup} where id == {id};
            """
        ctx.execute(q);