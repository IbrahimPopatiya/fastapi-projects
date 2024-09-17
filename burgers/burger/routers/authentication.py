from fastapi import APIRouter,Depends,status,HTTPException,Form
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,models,database,token
from ..hashing import Hash
from sqlalchemy.orm import Session
router = APIRouter(
  prefix="/login",
  tags=['Authentication']
)

@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(),role: str = Form(...), db: Session = Depends(database.get_db)):
  if role == "manager":
    manager = db.query(models.Manager).filter(models.Manager.email == request.username).first()
    if not manager:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid manager credentials")
    if not Hash.verify(manager.password,request.password):
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    #generate jwt token and return it
    access_token = token.create_access_token(data={"sub": manager.email},role="manager")
    return {"access_token":access_token, "token_type":"bearer"}
    
  
  elif role == "customer":
    customer = db.query(models.Customer).filter(models.Customer.email == request.username).first()
    if not customer:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid customer credentials")
    if not Hash.verify(customer.password,request.password):
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    #generate jwt token and get it
    
    access_token = token.create_access_token(data={"sub": customer.email},role="customer")
    return {"access_token":access_token, "token_type":"bearer"}
    