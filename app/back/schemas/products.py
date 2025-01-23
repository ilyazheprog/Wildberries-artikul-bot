from typing import Optional

from pydantic import BaseModel

from .out import ORMSchema

class ProductCreate(BaseModel):
    artikul: int
    name: str
    price_in_copecs: int
    rate: float
    total_quantity: int

class ProductUpdate(BaseModel):
    name: Optional[str]
    price_in_copecs: Optional[int]
    rate: Optional[float]
    total_quantity: Optional[int]

class ProductOut(ProductCreate, ORMSchema):
    pass