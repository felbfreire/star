from httpx import Client
import pytest


url = 'http://localhost:8000'

class TestCli():

    def test_homepage_statuscodo_200(self):
        with Client(base_url=url) as client:
            status_code = client.get('/').status_code
            assert status_code == 200
