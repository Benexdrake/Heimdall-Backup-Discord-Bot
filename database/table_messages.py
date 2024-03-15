from database.db_context import DbContext

class TableMessages:
    def get(self,id):
        db = DbContext.connect_database()
        cursor = db.cursor()

        guild = cursor.execute(f"select * from Guilds where id == {id}").fetchall()
        if len(guild) > 0:
            print(guild)
        db.close()
        return guild
    
    def insert_update(self,id, name, invite):
        guild = self.get_guild(id)
        db = DbContext.connect_database()
        cursor = db.cursor()
        q = ""
        if len(guild) == 0:
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
