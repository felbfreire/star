import sqlite3

import pytest

from httpx import Client


def connected_cursor():
    connection = sqlite3.connect('star.db')
    cursor = connection.cursor()
    return cursor

def create_table():
    query = 'create table stars(id integer primary key, star_name char(30));'
    cursor = connected_cursor()
    cursor.execute(query)
    cursor.connection.close()

def drop_table():
    cursor = connected_cursor()
    cursor.execute('drop table if exists stars;')
    cursor.connection.close()


url = 'http://localhost:8000'

class TestCli():

    def test_homepage_statuscode_200(self):
        with Client(base_url=url) as client:
            response = client.get('/')
            assert response.status_code == 200

    def test_homepage_method_post_should_return_405(self):
        with Client(base_url=url) as client:
            response = client.post('/')
            assert response.status_code == 405

    def test_userpage_greets_user(self):
        with Client(base_url=url) as client:
            user = 'Alfred'
            response = client.get('/{}'.format(user))
            assert response.status_code == 200
            assert response.content == b'Hello Alfred'

    def test_send_star(self):
        create_table()
        with Client(base_url=url) as client:
            client.post('/api/throw/Deathstar')
            response = client.get('api/stars')
            stars = response.json()
            assert response.status_code == 200
            assert stars[-1] == {'index': 1, 'star_name': 'Deathstar'}
        drop_table()
