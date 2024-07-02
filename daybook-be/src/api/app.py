from fastapi import FastAPI

from src.api.routes import auth, callbacks

app = FastAPI(title="DayBook API")
app.openapi_version = "1.0.0"

app.include_router(auth.router)
app.include_router(callbacks.router)
