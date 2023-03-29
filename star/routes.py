from starlette.routing import Route

from pages import homepage


routes = [
        Route('/', endpoint=homepage)
    ]

