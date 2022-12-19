from pydantic import BaseModel
from uuid import UUID

# schema for your signup
class Usersauth(BaseModel):
    id: int
    name: str
    password: str


# schema for user signup response
class Displayuser(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# schema for user logging
class Userinfo(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None


class Tokendata(BaseModel):
    name: str

class Userindb(BaseModel):
    hash_password: str
