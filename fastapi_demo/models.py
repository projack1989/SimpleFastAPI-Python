# models.py
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    price = Column(Float)
    description = Column(String(100), nullable=True)
    tipe = Column(String(50), nullable=True)     # kolom baru
    status = Column(String(50), nullable=True)   # kolom baru
