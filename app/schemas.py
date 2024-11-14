from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    #id : int
    name: str
    email: str
    info_user: str
    pass_user: str

    class Config:
        orm_mode = True 