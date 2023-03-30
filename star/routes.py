from starlette.routing import Route

from pages import homepage, UserPage


routes = [
        Route('/', endpoint=homepage, methods=['GET']),
        Route('/{username}', endpoint=UserPage, methods=['GET'])
    ]

