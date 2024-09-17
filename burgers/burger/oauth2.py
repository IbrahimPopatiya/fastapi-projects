from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
  credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
  
  return token.verify_token(token,credentials_exception)

def get_current_customer(token_str: str = Depends(oauth2_scheme)):
    user = get_current_user(token_str)
    if user.role != "customer":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized as a customer")
    return user
  


def get_current_manager(token_str: str = Depends(oauth2_scheme)):
    user = get_current_user(token_str)
    if user.role != "manager":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized as a manager")
    return user