from fastapi import FastAPI, Depends
from sql_app.database import SessionLocal
from routes import routes
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)

