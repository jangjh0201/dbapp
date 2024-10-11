from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    storage: bool

    class Config:
        from_attributes = True
