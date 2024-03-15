import sqlite3

import os
from dotenv import load_dotenv

class DbContext:
    def __init__(self):
        load_dotenv()

    def connect_database(self):
        databaseName:str = os.getenv("DBNAME")
        return sqlite3.connect(databaseName)
        

    def load_database(self):
        db_name:str = os.getenv("DBNAME")
        if db_name == '':
            print("Missing DBNAME in .env")
            return 

        if os.path.isfile(db_name) == False:
            print(f"Creating Database: {db_name}")
            self.create_database()

    def create_database(self):
        db = self.connect_database()
        cursor = db.cursor()
        table_guilds = """
        create table Guilds
        (
	        id bigint primary key,
            guildName varchar(128),
            inviteUrl varchar(128)
        );"""

        table_channels = """
        create table Channels
        (
	        id bigint primary key,
            guildId bigint,
            hasBackup boolean,
            constraint fk_Guild_Channel foreign key(guildId) references Guilds(id) 
        );"""
        
        table_messages = """
        create table Messages
        (
        	id bigint primary key,
            channelId bigint,
            hasFiles bool,
            message text,
            date_time datetime,
            userId bigint,
            constraint fk_Channel_Message foreign key(channelId) references Channels(id)
        );"""
        cursor.execute(table_guilds)
        cursor.execute(table_channels)
        cursor.execute(table_messages)
        db.commit()
        db.close()

    def insert_update_guild(self,id, name, invite):
        print("Get Guild")
        guild = self.get_guild(id)
        
        db = self.connect_database()
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

    def get_guild(self,id):
        db = self.connect_database()
        cursor = db.cursor()

        guild = cursor.execute(f"select * from Guilds where id == {id}").fetchall()
        if len(guild) > 0:
            print(guild)
        db.close()
        return guild
        




        