from contextlib import asynccontextmanager

from databases import Database

from config import DATABASE_URL, SCRIPT


async def connect_database():
    database = Database(DATABASE_URL)
    await database.connect()
    return database

@asynccontextmanager
async def lifespan(app):
    database = await connect_database()
    await database.connect()
    yield
    await database.disconnect()

async def init_db():
    async with Database(DATABASE_URL) as database:
        with open(SCRIPT, 'r') as file:
            for line in file:
                if line:
                    await database.execute(line)
            await database.disconnect()

