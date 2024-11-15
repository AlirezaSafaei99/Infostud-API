# schemas.py
# This file defines Pydantic models (schemas) for request and response data validation.
# The schemas ensure that data received from and sent to the API conforms to a specified structure.
# The UserBase schema, for instance, defines the structure of a user object in API responses.

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id : int
    name: str
    email: str
    info_user: str
    pass_user: str

    class Config:
        orm_mode = True 