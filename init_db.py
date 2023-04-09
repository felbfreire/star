import sqlite3


def connected_cursor():
    connection = sqlite3.connect('star.db')
    cursor = connection.cursor()
    return cursor

def drop_cursor(cursor):
    cursor.connection.commit()
    cursor.connection.close()

def init_db():
    #query = ('create table stars(id integer primary key, star_name char(30));')
    with open('script.sql', 'r') as file:
        cursor = connected_cursor()
        for line in file:
            if line:
                cursor.execute(line)
        cursor.connection.commit()

if __name__ == '__main__':
    init_db()

