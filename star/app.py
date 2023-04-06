from starlette.applications import Starlette

from db import lifespan
from routes import routes



app = Starlette(
        routes=routes,
        lifespan=lifespan
        )

