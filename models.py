from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "Jompre"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
