from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    info_user: str
    pass_user: str

    class Config:
        orm_mode = True 