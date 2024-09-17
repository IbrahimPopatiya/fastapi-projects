from fastapi import FastAPI, Depends,status,Response,HTTPException,Query
from . import schemas, models,hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import Menu,Order,Customer,Manager,authentication
# models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(Menu.router)
app.include_router(Order.router)
app.include_router(Customer.router)
app.include_router(Manager.router)

# def get_db(): 
#   db = SessionLocal() 
#   try:
#     yield db 
#   finally:
#     db.close()  


#create dish
# @app.post('/resturant/menu',status_code=status.HTTP_201_CREATED,tags=['Menu'])
# def add_dish(dish: schemas.Dish,db: Session = Depends(get_db)):
#   new_dish = models.Dish(name=dish.name,price=dish.price)
#   db.add(new_dish)
#   db.commit()
#   db.refresh(new_dish)
#   return new_dish


# @app.get('/resturant/menu',tags=['Menu'])
# def Menu(db:Session = Depends(get_db)):
#   menu = db.query(models.Dish).all()
#   return menu

# @app.put('/resturant/menu/{id}',tags=['Menu'])
# def update_menu(id,dish:schemas.Dish,db:Session = Depends(get_db)):
#   update_dish_menu = db.query(models.Dish).filter(models.Dish.id == id).first()
#   if not update_dish_menu:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"dish not in menu")
#   if dish.name is not None:
#     update_dish_menu.name = dish.name
#   if dish.price is not None:  
#     update_dish_menu.price = dish.price
#   db.commit()
#   return 'updated'




# @app.get('/resturant/order/{id}',status_code=200,tags=['Order'])
# def get_order(id,quantity:int ,tablenumber:int, db:Session = Depends(get_db)):
#   customer = db.query(models.Customer).filter(models.Customer.tablenumber == tablenumber).first()
    
#   if not customer:
#       raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Customer with table number {tablenumber} not found.")
#   dish = db.query(models.Dish).filter(models.Dish.id == id).first()

#   if not dish:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Dish is not available")
  
#   new_order = models.Order(name=dish.name,price=dish.price,quantity=quantity,tablenumber=tablenumber)
#   db.add(new_order)
#   db.commit()
#   db.refresh(new_order)

#   menu = db.query(models.Dish).all()

  
    

#   return {
#     "selected dish": new_order,
#     "menu": menu
#   }

# @app.post('/resturant/order',tags=['Order'])
# def my_order(db:Session = Depends(get_db)):
#   customer_order = db.query(models.Order).all()
#   return customer_order


# @app.delete('/resturant/order/{name}',tags=['Order'])
# def delete_order(name,db:Session = Depends(get_db)):
#   dish = db.query(models.Order).filter(models.Order.name == name)
#   if not dish.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} not in Menu")
#   dish.delete(synchronize_session=False)
#   db.commit()
#   return 'done'


# @app.put('/resturant/order/{name}',tags=['Order'])
# def update_order(name,dish:schemas.Dish,db:Session = Depends(get_db)):
#   update_dish = db.query(models.Order).filter(models.Order.name==name).first()
#   if not update_dish:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} is not in Order")
#   menu_dish = db.query(models.Dish).filter(models.Dish.name == dish.name).first()
#   if not menu_dish:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} is not in Menu")
  
#   update_dish.name = menu_dish.name
#   update_dish.price = menu_dish.price

  
#   db.commit()
#   return {"message": "Order updated successfully", "updated_order": update_dish.name}

# @app.delete('/resturant/menu{name}',tags=['Menu'])
# def delete_menu(name,db:Session = Depends(get_db)):
#   del_dish = db.query(models.Dish).filter(models.Dish.name == name).first()
#   if not del_dish:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{name} not found in menu")
#   db.delete(del_dish)
#   db.commit()
#   return {"message":'Sussesfully deleted',
#           "deleted Dish": del_dish}


# @app.post('/customer',tags=['Customers'])
# def create_Customer(request: schemas.Customer,db: Session = Depends(get_db)):
#   customer = models.Customer(tablenumber=request.tablenumber,email=request.email,password=hashing.Hash.bcrypt(request.password))
#   db.add(customer)
#   db.commit()
#   db.refresh(customer)
#   return customer

# @app.get('/customer/{tablenumber}',tags=['Customers'])
# def get_customer(tablenumber:int,db:Session = Depends(get_db)):
#   customers = db.query(models.Customer).filter(models.Customer.tablenumber == tablenumber).first()
#   if not customers:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with table number {tablenumber} not available")
  
#   orders = db.query(models.Order).filter(models.Order.tablenumber == tablenumber).all()

#   return {
#     "customer": {
#       "tablenumber": customers.tablenumber,
#     },
#     "orders": orders
#   }



# @app.post('/manager',tags=['Managers'])
# def create_manager(request: schemas.Manager,db: Session = Depends(get_db)):
  
#   manager = models.Manager(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
#   db.add(manager)
#   db.commit()
#   db.refresh(manager)
#   return manager