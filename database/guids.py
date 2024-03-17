from database.db_context import DbContext
import json

import os
from dotenv import load_dotenv

class Guids:
    def __init__(self):
        load_dotenv()

    async def get(self, guid):
        ctx = DbContext()
        q = f"""
                select guid from guids where guid = '{guid}';
            """
        return ctx.execute(q);

    async def insert(self,guid):

        ctx = DbContext()
        q = f"""
                insert into guids values ('{guid}');
            """
        ctx.execute(q);

    async def delete(self, guid):
        ctx = DbContext()
        q = f"""
            delete from guids where guid = '{guid}';
            """
        ctx.execute(q);