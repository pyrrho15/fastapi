from sqlalchemy import column, create_engine, Column, Integer, String, true
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app=FastAPI()
DB_URL="sqlite:///./test.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    completed=Column(String)

Base.metadata.create_all(bind=engine) 

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
@app.get("/")
def home(db:Session=Depends(get_db)):
    return{
        "message":"DB CONNECTED"
    }