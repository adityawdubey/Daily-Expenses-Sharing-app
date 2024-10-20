from fastapi import FastAPI
from app.api.endpoints import users
from app.api.endpoints import expenses

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)
