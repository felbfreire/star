from databases import Database


DB_FILE = '../star.db'
SCRIPT = '../script.sql'
DATABASE = 'sqlite+aiosqlite:///{}'

async def connect_database():
    database = Database(DATABASE.format(DB_FILE))
    await database.connect()
    return database

async def init_db():
    async with Database(DATABASE.format(DB_FILE)) as database:
        with open(SCRIPT, 'r') as file:
            for line in file:
                if line:
                    await database.execute(line)
            await database.disconnect()

