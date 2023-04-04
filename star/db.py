from databases import Database


DB = '../star.db'
SCRIPT = '../script.sql'

async def connect_database():
    database = Database('sqlite+aiosqlite:///{}'.format(DB))
    await database.connect()
    return database

async def init_db():
    database = await connect_database()
    with open(SCRIPT, 'r') as file:
        for line in file:
            if line:
                await database.execute(line)

