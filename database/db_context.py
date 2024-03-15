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
        tables = """
        create table Guilds
        (
	        id bigint primary key,
            guildName varchar(128),
            inviteUrl varchar(128)
        );
        create table Channels
        (
	        id bigint primary key,
            guildId bigint,
            hasBackup boolean,
            constraint fk_Guild_Channel foreign key(guildId) references Guilds(id) 
        );
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
        print('Create DB')
        self.execute(tables)

    def execute(self,query:str):
        db = self.connect_database()
        cursor = db.cursor()
        cursor.executescript(query)
        result = cursor.fetchall()

        db.commit()
        db.close()

        return result  
        





        