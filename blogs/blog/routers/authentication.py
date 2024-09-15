from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,database,models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
  tags=["Authentication"]
)
# get_db = database.get_db

@router.post('/login')
# here request not be schemas.Login it should be Oauth2...
# when doing oauth change request from schemas.Logint to oauth2pass....
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
  if not Hash.verify(user.password,request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Password")

  # generate a jwt token and return
  access_token = token.create_access_token(data={"sub": user.email})
  return {"access_token":access_token, "token_type":"bearer"}
 