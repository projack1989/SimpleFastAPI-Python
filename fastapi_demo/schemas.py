# schemas.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
