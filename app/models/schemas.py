from pydantic import BaseModel
from typing import List, Optional


class Beverage(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True


class Consumable(BaseModel):
    id: int
    name: str
    storage: bool

    class Config:
        from_attributes = True


class User(BaseModel):
    username: str
    password: str


FAKE_USERS_DB = {
    "rbiz": {
        "username": "rbiz",
        "password": "xyz",  # 실제로는 해시된 비밀번호를 사용해야 합니다.
    }
}
