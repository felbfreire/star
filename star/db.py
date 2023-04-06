from starlette.config import Config

from databases import Database


config = Config('.env')
DB_FILE = '../star.db'
SCRIPT = '../script.sql'
DATABASE = 'sqlite+aiosqlite:///{}'
DATABASE_URL = config('DATABASE_URL')

async def connect_database():
    database = Database(DATABASE_URL)
    await database.connect()
    return database

async def init_db():
    async with Database(DATABASE_URL) as database:
        with open(SCRIPT, 'r') as file:
            for line in file:
                if line:
                    await database.execute(line)
            await database.disconnect()

