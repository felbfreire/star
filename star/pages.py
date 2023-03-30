from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint


async def homepage(request): 
    return PlainTextResponse("Homepage") # Response

class UserPage(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse('Hello {}'.format(username))

