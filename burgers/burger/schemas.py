#response model help to hide that not want to show

from pydantic import BaseModel
from typing import Optional,List


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

