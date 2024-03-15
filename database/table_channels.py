from database.db_context import DbContext

class TableChannels:
    def get(self,id):
        db = DbContext.connect_database()
        cursor = db.cursor()
        channel = cursor.execute(f"select * from Channels where id == {id}").fetchall()
        db.close()
        return channel
    
    def insert_update(self,id, name, invite):
        channel = self.get(id)
        db = DbContext.connect_database()
        cursor = db.cursor()
        q = ""
        if len(channel) == 0:
            print("Insert Guild")
            q = f"""
                insert into guilds values ({id},'{name}','{invite}')
                """
        else:
            print("Update Guild")
            q = f"""
                update guilds set id = {id}, guildName = '{name}', inviteUrl = '{invite}' where id = {id}
                """
        cursor.execute(q);
        db.commit()
        db.close()

    def drop(self,id):
        db = DbContext.connect_database()
        cursor = db.cursor()
        pass        
