from fastapi import APIRouter,Depends,status, HTTPException
from typing import List
from .. import schemas,database,models
from ..hashing import Hash
from sqlalchemy.orm import Session
from passlib.context import CryptContext


router = APIRouter(
  prefix="/user",
  tags=["User"]
)
get_db = database.get_db




#encrypt the password and hide it
#move to hashing.py
# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #2

# create user

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
  # hashedPassword = pwd_cxt.hash(request.password) #3
  new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password)) 
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


#get user with id
@router.get('/{id}',response_model=schemas.ShowUser)
def show_user(id,db: Session = Depends(get_db)):
  user_id = db.query(models.User).filter(models.User.id == id).first()
  if not user_id:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not exsist")
  return user_id