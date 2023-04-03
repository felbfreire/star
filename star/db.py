from asyncio import run
from databases import Database


database = Database('sqlite+aiosqlite:///star.db')
query = 'create table stars(id integer primary key, star_name char(30) not null)'

async def main():
        await database.connect()
        await database.execute(query)

if __name__ == '__main__':
    run(main())
