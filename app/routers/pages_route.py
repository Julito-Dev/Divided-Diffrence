from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/", response_class=FileResponse)
def home():
    return FileResponse("app/static/index.html")

