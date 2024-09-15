from typing import List
from fastapi import FastAPI, Depends,status,Response, HTTPException
from . import schemas ,models
from blog.hashing import Hash
from blog.database import engine, get_db, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext # for password
from blog.routers import blog #importing router in main.py from routers/blog 
from blog.routers import user #importing router in main.py from routers/user 
from blog.routers import authentication
app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

























models.Base.metadata.create_all(engine) # create table in database


#while using api router get_db is shifted to database and abstracting from it
# in line 4 get_db


# def get_db(): # function
#   db = SessionLocal() #from database
#   try:
#     yield db #
#   finally:
#     db.close()  


#move to api router in routers/blog file
#create blog
# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["blogs"])#direct --> status_code=201
# def create(request: schemas.Blog, db: Session = Depends(get_db)):# db is instance #db is type of session # depends convert session into pydantic type
#   new_blog = models.Blog(title=request.title,   body=request.body,user_id=1)#going to be schema(model), user_id from relationship part
#   db.add(new_blog)#add model to db
#   db.commit()#execute it
#   db.refresh(new_blog)#refresh
#   return new_blog




#move to api router in routers/blog file
#delete the blog with id
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
# def delete(id, db:Session = Depends(get_db)):
#   blog = db.query(models.Blog).filter(models.Blog.id == id)
#   if not blog.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
#   blog.delete(synchronize_session=False)
#   db.commit()
#   return 'done'


#move to api router in routers/blog file
#update the blog with id
# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
# def update(id,request: schemas.Blog, db:Session = Depends(get_db)):
#   blog = db.query(models.Blog).filter(models.Blog.id == id)
#   if not blog.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#   blog.update(request.dict())
#   db.commit()
#   return 'updated'



#get blog from database
# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=["blogs"])
# def all(db: Session = Depends(get_db)): #database instance
#   blogs = db.query(models.Blog).all() #get all blogs
#   return blogs




#move to api router in routers/blog file
# #get blog with id
# @app.get('/blog/{id}', status_code=200,response_model=schemas.ShowBlog,tags=["blogs"])
# def show(id, response: Response, db: Session = Depends(get_db)): #session is db instance and depend also act as  default value
#   blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#   if not blog:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not available") # can be raise using http
#     # response.status_code = status.HTTP_404_NOT_FOUND
#     # return {'detail':f"blog with id {id} not available"}
#   return blog




# #encrypt the password and hide it
# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #2


#move to api router in routers/blog file

# # create user
# # in this showUser only show email amd name in response
# @app.post('/user',response_model=schemas.ShowUser,tags=["User"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#   hashedPassword = pwd_cxt.hash(request.password) #3
#   new_user = models.User(name=request.name,email=request.email,password=hashedPassword) #4forpassword
#   db.add(new_user)
#   db.commit()
#   db.refresh(new_user)
#   return new_user




#move to api router in routers/blog file
# #get user with id
# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=["User"])
# def show_user(id,db: Session = Depends(get_db)):
#   user_id = db.query(models.User).filter(models.User.id == id).first()
#   if not user_id:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not exsist")
#   return user_id


import uvicorn
if __name__ == "__main__":
  uvicorn.run(app = app, host="localhost",port=3000)