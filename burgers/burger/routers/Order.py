from fastapi import APIRouter,Depends,status,HTTPException,Form
from .. import schemas,models,database,oauth2
from sqlalchemy.orm import Session


router = APIRouter(
  tags=['Order']
)


get_db = database.get_db



@router.get('/resturant/order/{id}',status_code=200)
def get_order(id,quantity:int ,tablenumber:int, db:Session = Depends(get_db)):
  customer = db.query(models.Customer).filter(models.Customer.tablenumber == tablenumber).first()
    
  if not customer:
      raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with table number {tablenumber} not found.")
  dish = db.query(models.Dish).filter(models.Dish.id == id).first()

  if not dish:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Dish is not available")
  
  new_order = models.Order(name=dish.name,price=dish.price,quantity=quantity,tablenumber=tablenumber)
  db.add(new_order)
  db.commit()
  db.refresh(new_order)

  menu = db.query(models.Dish).all()

  
    

  return {
    "selected dish": new_order,
    "menu": menu
  }

@router.post('/resturant/order')
def my_order(db:Session = Depends(get_db),current_customer: schemas.Customer = Depends(oauth2.get_current_customer),tablenumber:int = Form(...)):
  customer_order = db.query(models.Order).filter(models.Order.tablenumber == tablenumber).all()
  return customer_order


@router.delete('/resturant/order/{name}')
def delete_order(name,db:Session = Depends(get_db)):
  dish = db.query(models.Order).filter(models.Order.name == name)
  if not dish.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} not in Menu")
  dish.delete(synchronize_session=False)
  db.commit()
  return 'done'

@router.put('/resturant/order/{name}')
def update_order(name,dish:schemas.Dish,db:Session = Depends(get_db)):
  update_dish = db.query(models.Order).filter(models.Order.name==name).first()
  if not update_dish:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} is not in Order")
  menu_dish = db.query(models.Dish).filter(models.Dish.name == dish.name).first()
  if not menu_dish:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} is not in Menu")
  
  update_dish.name = menu_dish.name
  update_dish.price = menu_dish.price

  
  db.commit()
  return {"message": "Order updated successfully", "updated_order": update_dish.name}