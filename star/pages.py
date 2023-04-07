from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from db import list_stars


async def homepage(request): 
    return PlainTextResponse("Homepage") # Response

class UserPage(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse('Hello {}'.format(username))

async def stars(request):
    stars = await list_stars()
    return JSONResponse(str(stars))

