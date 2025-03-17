from fastapi import FastAPI
from app.apis.user import router as user_router

# entry point
app = FastAPI()

app.include_router(user_router)