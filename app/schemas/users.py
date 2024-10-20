from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    mobile: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True

