import os
from dotenv import load_dotenv

class CheckEnv:
    def __init__(self):
        load_dotenv()
    
    def check(self):
        dotenv_path = os.path.join(os.getcwd(), ".env")

        if not os.path.exists(dotenv_path):
            with open(dotenv_path, "w") as f:
                print('Creating .env File for Configurations')
                f.write("")
                load_dotenv()

        if os.getenv('BOTTOKEN') is None:
            with open(dotenv_path, "a") as f:
                print('Adding BOTTOKEN into .env')
                f.write("BOTTOKEN='INSERT_TOKEN_HERE'\n")
        
        if os.getenv('DBNAME') is None:
            print('Adding DBNAME into .env')
            with open(dotenv_path, "a") as f:
                f.write("DBNAME='helheim.db'\n")

        if os.getenv('FILESPATH') is None:
            print('ADDING FILESPATH into .env')
            with open(dotenv_path, "a") as f:
                f.write("FILESPATH='FILES'\n")
        
        if os.getenv('MIDGARDCHANNEL') is None:
            with open(dotenv_path, "a") as f:
                f.write(f"MIDGARDCHANNEL='idavoll'\n")

        if os.getenv('LOG') is None:
            with open(dotenv_path, "a") as f:
                f.write(f"LOG=' '\n")

        if os.getenv('INVITE') is None:
            with open(dotenv_path, "a") as f:
                f.write(f"INVITE=' '\n")