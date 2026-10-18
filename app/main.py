from fastapi import FastAPI
from app.routers import pages_route

app = FastAPI()

app.include_router(pages_route.router)
