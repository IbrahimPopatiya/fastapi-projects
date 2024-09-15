from fastapi import FastAPI,Path,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  brand: Optional[str] = None

class UpdateItem(BaseModel):
  name: Optional[str] = None
  price: Optional[float] = None
  brand: Optional[str] = None

inventory = {
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int= Path(... ,description="the ID of the item you like to view", gt=0, lt=2000)):
  return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
  for item_id in inventory:
    if inventory[item_id].name == name:
      return inventory[item_id]
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item name not found")  







@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
  if item_id in inventory:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item id already exixts")
  
  inventory[item_id] = item#{"name": item.name, "brand":item.brand, "price": item.price}
  return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
  if item_id not in inventory:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item id not exixts")
  if item.name != None:
    inventory[item_id].name = item.name
  if item.price != None:
    inventory[item_id].price = item.price
  if item.brand != None:
    inventory[item_id].brand = item.brand    
  return inventory[item_id]


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int = Path(...,description="The ID of the item to delete", gt=0,lt = 2000)):
  if item_id not in inventory:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID does not exist")
  del inventory[item_id]
  return {"Success": "Item deleted!"}