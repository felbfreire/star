from starlette.routing import Route

from pages import homepage, UserPage, stars


routes = [
        Route('/', endpoint=homepage, methods=['GET']),
        Route('/{username}', endpoint=UserPage, methods=['GET']),
        Route('/api/stars', endpoint=stars, methods=['GET']),
    ]

