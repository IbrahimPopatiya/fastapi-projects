#response model help to hide that not want to show

from pydantic import BaseModel
from typing import Optional,List,Literal


class Dish(BaseModel):
  name:Optional[str] = None
  price:Optional[str] = None
  

  class Config:
    from_attributes = True


class Order(BaseModel):
  name:Optional[str] = None
  price:Optional[str] = None
  quantity: Optional[int] = None

  class Config:
    from_attributes = True

class Manager(BaseModel):
  name: str
  email:str
  password:str
  # role: str = "Manager"

class Customer(BaseModel):
  tablenumber: int
  email:str
  password:str
  orders: List[Order]=[]
  # role: str = "Manager"  
  class Config:
        from_attributes = True

class Login(BaseModel):
   username: str
   password: str
   role: Literal["manager","customer"]



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None   