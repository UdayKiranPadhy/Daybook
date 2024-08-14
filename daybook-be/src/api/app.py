from fastapi import FastAPI

from src.api.routes import auth, callbacks

app = FastAPI(title="DayBook API")

app.include_router(auth.router)
app.include_router(callbacks.router)
from src.api.dependencies import container

@app.get("/")
def hello():
    print("Hello, World!")
    return {"message": "Hello, World!"}