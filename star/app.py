from starlette.applications import Starlette

from db import init_db
from routes import routes



app = Starlette(
        routes=routes,
        on_startup=[init_db]
        )

