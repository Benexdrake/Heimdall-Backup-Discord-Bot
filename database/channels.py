from database.db_context import DbContext
import json

import os
from dotenv import load_dotenv

class Channels:
    def __init__(self):
        load_dotenv()

    async def get(self, id):
        ctx = DbContext()
        q = f"""
                select * from channels where id = {id};
            """
        return ctx.execute(q);

    async def insert(self,channel):
        ignore_list = []
        with open("serverIgnoreList.json", "r") as f:
            data = json.load(f)
            ignore_list = data["Ignore"]

        if channel.guild.id == int(os.getenv('YGGDRASILID')) or channel.name in ignore_list or channel.name == os.getenv('MIDGARDCHANNEL').lower():
            return

        ctx = DbContext()
        q = f"""
                insert into channels values ({channel.id},{channel.guild.id},'{channel.name}');
            """
        ctx.execute(q);

    async def update(self,channel):
        ctx = DbContext()
        q = f"""
            update channels set name = '{channel.name}' where id == {channel.id};
            """
        ctx.execute(q);

    async def delete(self, channel):
        ctx = DbContext()
        q = f"""
            delete from channels where id = {channel.id};
            """
        ctx.execute(q);