from fastapi import FastAPI
from app.api import users, expenses

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)
