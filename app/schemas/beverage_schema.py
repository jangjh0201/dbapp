from pydantic import BaseModel


class Beverage(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True
