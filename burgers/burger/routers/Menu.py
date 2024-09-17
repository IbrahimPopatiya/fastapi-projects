from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session


router = APIRouter(
  tags=['Menu']
)


get_db = database.get_db

@router.get('/resturant/menu')
def Menu(db:Session = Depends(get_db)):
  menu = db.query(models.Dish).all()
  return menu
  


@router.post('/resturant/menu',status_code=status.HTTP_201_CREATED)
def add_dish(dish: schemas.Dish,db: Session = Depends(get_db)):
  new_dish = models.Dish(name=dish.name,price=dish.price)
  db.add(new_dish)
  db.commit()
  db.refresh(new_dish)
  return new_dish


@router.put('/resturant/menu/{id}')
def update_menu(id,dish:schemas.Dish,db:Session = Depends(get_db)):
  update_dish_menu = db.query(models.Dish).filter(models.Dish.id == id).first()
  if not update_dish_menu:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"dish not in menu")
  if dish.name is not None:
    update_dish_menu.name = dish.name
  if dish.price is not None:  
    update_dish_menu.price = dish.price
  db.commit()
  return 'updated'

@router.delete('/resturant/menu{name}')
def delete_menu(name,db:Session = Depends(get_db)):
  del_dish = db.query(models.Dish).filter(models.Dish.name == name).first()
  if not del_dish:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} not found in menu")
  db.delete(del_dish)
  db.commit()
  return {"message":'Sussesfully deleted',
          "deleted Dish": del_dish}