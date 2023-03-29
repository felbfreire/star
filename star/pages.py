from starlette.responses import PlainTextResponse


async def homepage(request):
    return PlainTextResponse("Homepage")
