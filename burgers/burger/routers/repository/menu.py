from sqlalchemy.orm import Session
from burger import models

def get_menu(db: Session):
  menu = db.query(models.Dish).all()
  return menu