from typing import Optional
from pydantic import BaseModel

# Entidad user
class User(BaseModel):
    Username: str
    fullname: str
    email: str
    disabled: str
    password: str