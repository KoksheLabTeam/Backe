from fastapi import FastAPI

from app.apis.routers import routers

app = FastAPI()

app.include_router(routers)
