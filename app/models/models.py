from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    mobile = Column(String, unique=True)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    split_method = Column(Enum('equal', 'exact', 'percentage'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
