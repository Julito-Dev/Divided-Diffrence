from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from app.routers import pages_route

app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join("app", "static")), name="static")

app.include_router(pages_route.router)
