from sqlalchemy import create_engine #endine
from sqlalchemy.ext.declarative import declarative_base # mapping
from sqlalchemy.orm import sessionmaker # talk to database

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db' #path

engine  = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False},pool_pre_ping=True) #creating engine

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()

#api router using
def get_db(): # function
  db = SessionLocal() #from database
  try:
    yield db #
  finally:
    db.close()  