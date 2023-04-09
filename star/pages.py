from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from db import list_stars, push_star


async def homepage(request): 
    return PlainTextResponse("Homepage")

class UserPage(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse('Hello {}'.format(username))

async def stars(request):
    stars = await list_stars()
    return JSONResponse(stars)

async def send_star(request):
    try:
        star = request.path_params['star_name']
    except KeyError:
        return PlainTextResponse('[star_name] not found.')

    await push_star(
                star_name='{}'.format(star)
            )
    return PlainTextResponse('insert {}'.format(star))

