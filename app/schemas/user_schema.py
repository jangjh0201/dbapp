from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


FAKE_USERS_DB = {
    "rbiz": {
        "username": "rbiz",
        "password": "xyz",  # 실제로는 해시된 비밀번호를 사용해야 합니다.
    }
}
