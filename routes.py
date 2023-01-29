from fastapi import APIRouter
from virtual_internship import app


routes = APIRouter()

routes.include_router(app.router, prefix="/app")