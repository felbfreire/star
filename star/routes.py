from starlette.routing import Route

from pages import homepage, UserPage, stars, send_star


routes = [
        Route('/', endpoint=homepage, methods=['GET']),
        Route('/{username}', endpoint=UserPage, methods=['GET']),
        Route('/api/stars', endpoint=stars, methods=['GET']),
        Route('/api/throw/{star_name}', endpoint=send_star, methods=['GET', 'POST']),
    ]

