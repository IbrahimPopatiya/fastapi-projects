from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,database,hashing
from sqlalchemy.orm import Session
router = APIRouter(
  prefix="/customer",
  tags=['Customers']
)
get_db = database.get_db




@router.post('/')
def create_Customer(request: schemas.Customer,db: Session = Depends(get_db)):
  customer = models.Customer(tablenumber=request.tablenumber,email=request.email,password=hashing.Hash.bcrypt(request.password))
  db.add(customer)
  db.commit()
  db.refresh(customer)
  return customer

@router.get('/{tablenumber}')
def get_customer(tablenumber:int,db:Session = Depends(get_db)):
  customers = db.query(models.Customer).filter(models.Customer.tablenumber == tablenumber).first()
  if not customers:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with table number {tablenumber} not available")
  
  orders = db.query(models.Order).filter(models.Order.tablenumber == tablenumber).all()

  return {
    "customer": {
      "tablenumber": customers.tablenumber,
    },
    "orders": orders
  }