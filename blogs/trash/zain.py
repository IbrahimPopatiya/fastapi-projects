from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
  name:str
  body:str

@app.post('/blog')
def create_blog(blog: Blog):
  return blog.name