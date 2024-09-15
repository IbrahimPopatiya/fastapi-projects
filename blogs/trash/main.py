#request body --1.post 2.get
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

# ?--> Query parameter
@app.get('/blog') #path-decorator.operation(path)
def index(limit=10,published: bool=False, sort:Optional[str] = None): # path operation function
  if published:
    return {"data": f'{limit} published blogs from db list'}
  else:
    return {"data": f'{limit} blogs from db list'}

@app.get('/blog/unpublished')
def unpublished():
  return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id:int):
  return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id:int):
  return {id: {id,'2'}}

class Blog(BaseModel):
  title:str
  body:str
  published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
  return blog.body
  