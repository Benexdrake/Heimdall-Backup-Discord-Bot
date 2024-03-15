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
        guilds = """
        create table Guilds
        (
	        id bigint primary key,
            guildName varchar(128),
            inviteUrl varchar(128)
        );
        """

        channels = """
        create table Channels
        (
	        id bigint primary key,
            guildId bigint,
            hasBackup boolean,
            constraint fk_Guild_Channel foreign key(guildId) references Guilds(id) 
        );
        """

        messages = """
        create table Messages
        (
        	id bigint primary key,
            channelId bigint,
            hasFiles bool,
            message text,
            date_time datetime,
            userId bigint,
            constraint fk_Channel_Message foreign key(channelId) references Channels(id)
        );
        """
        self.execute(guilds)
        self.execute(channels)
        self.execute(messages)

    def execute(self,query:str):
        db = self.connect_database()
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        db.commit()
        db.close()

        return result  
        





        