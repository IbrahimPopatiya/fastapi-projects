from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,database,hashing
from sqlalchemy.orm import Session


router = APIRouter(
  prefix="/manager",
  tags=['Managers']
)

get_db = database.get_db

@router.post('/manager')
def create_manager(request: schemas.Manager,db: Session = Depends(get_db)):
  
  manager = models.Manager(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
  db.add(manager)
  db.commit()
  db.refresh(manager)
  return manager