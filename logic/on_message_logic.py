import os
from dotenv import load_dotenv
import requests

from database.messages import Messages

class OnMessageLogic:
    def __init__(self):
        load_dotenv()

    async def create(self, message):
        if(message.author.bot or message.author.system):
            return
        await Messages().insert(message)

        FILEPATH = os.getenv('FILESPATH')

        if len(message.attachments) > 0:
            path = f'./{FILEPATH}/{message.channel.guild.id}/{message.channel.id}/{message.id}'

            os.makedirs(path, exist_ok=True)
        
            for a in message.attachments:
                response = requests.get(a.url)
                with open(path+"/"+a.filename, "wb") as f:
                    f.write(response.content)