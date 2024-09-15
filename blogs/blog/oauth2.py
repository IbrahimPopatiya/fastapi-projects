# authentication to routes (security to  path )
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import token
# this is route/url from where fastapi will fetch the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(Data: str = Depends(oauth2_scheme)):
  #exception it has created
  credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
  )

  return token.verify_token(Data,credentials_exception)
  
  