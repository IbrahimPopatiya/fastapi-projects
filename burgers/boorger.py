from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Dish(BaseModel):
  dish_name:str
  price:str


#get all dish in the menu
@app.get('/resturant/menu')
def all_dishes():
  return {"message": "returning all dishes"}

#add Dish in menu
@app.post('/resturant/menu')
def add_Dish(dish: Dish):
  return dish

#place an order
@app.post('/resturant/order')
def my_order():
  return {"message": "order placed"}

@app.get('/resturant/order')
def get_order():
  return {"message": "all order"}

@app.put('/resturant')
def update_menu():
  return {"message": " menu updated"}

@app.put('/resturant')
def update_order():
  return {"message": " order updated"}

@app.delete('/resturant/order')
def delete_order():
  return {"message": "order deleted"}

@app.delete('/resturant/menu')
def delete_menu():
  return {"message": "dish deleted from menu"}




