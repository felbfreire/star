from contextlib import asynccontextmanager

from databases import Database

from config import DATABASE_URL, SCRIPT


async def create_database():
    database = Database(DATABASE_URL)
    await database.connect()
    return database

@asynccontextmanager
async def lifespan(app):
    database = await create_database()
    await database.connect()
    yield
    await database.disconnect()

async def list_stars():
    query = ('select * from stars;')
    database = await create_database()
    results = await database.fetch_all(query)

    content = [
            {
                "index": result["id"], "star_name": result["star_name"]
            } 
            for result in results
    ]
    return content

async def push_star(**kw):
    async with Database(DATABASE_URL) as database:
        star_name = kw['star_name']
        query = "insert into stars(star_name) values ('%s');"
        await database.execute((query % (star_name)))

