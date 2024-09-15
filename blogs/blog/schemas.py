from pydantic import BaseModel
from typing import List
from typing import Optional
class Blog(BaseModel):
  title:str
  body:str
  class Confiq(): # helps to convert in pydantic model it helps to retrive data from database
    orm_mode=True


class User(BaseModel):
  name:str
  email:str
  password:str

#show only name and email
class ShowUser(BaseModel):
  name:str
  email:str
  blogs : List[Blog] = [] #all blog created by user
  class Config():
    orm_mode=True


class ShowBlog(BaseModel):
  title:str
  body:str
  creator: ShowUser
  class Config():
    orm_mode=True


class Login(BaseModel):
  username: str
  password: str    

class Token(BaseModel):  
  access_token: str
  token_type: str


class TokenData(BaseModel):
  email: Optional[str] = None  