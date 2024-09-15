from sqlalchemy import Column , Integer , String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Dish(Base):
  __tablename__ = "Menu"
  id = Column(Integer,primary_key=True, index=True)
  name = Column(String)
  price = Column(String)
  # Quantity = Column(Integer)

class Order(Base):
  __tablename__ = "Order"
  id = Column(Integer,primary_key=True, index=True)
  name = Column(String)
  price = Column(Integer) 
  quantity = Column(Integer)
  tablenumber = Column(Integer, ForeignKey('Customers.tablenumber'))
  # table_number = Column(Integer)
 
  creator = relationship("Customer", back_populates="orders")
  
class Manager(Base):
  __tablename__ = "Managers"
  id = Column(Integer,primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)
  # role = Column(String, default="Manager")  

class Customer(Base):
  __tablename__ = "Customers"
  id = Column(Integer,primary_key=True, index=True)
  tablenumber = Column(Integer,unique=True)
  email = Column(String)
  password = Column(String)
  # role = Column(String, default="Customer")
  orders = relationship('Order',back_populates="creator")  