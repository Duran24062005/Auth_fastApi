from fastapi import FastAPI
from middlewares import core_middleware
from routes.auth_routes import auth_routes


app = FastAPI(
    title="Authentication in FastAPI",
    version="0.0.1"
)

core_middleware.app_cors(app)


app.include_router(auth_routes)