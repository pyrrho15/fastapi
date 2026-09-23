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
    
# CREATE
@app.post("/create_todo")
def create_todo(title:str,db:Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }

# READ
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "total":len(todos),
        "data":todos
    }

@app.get("/todos/{id}")
def get_todo_id(db:Session=Depends(get_db), id=int):

    todo = db.query(Todo).filter(Todo.id == id).first()
    
    return {"data":todo}

# UPDATE
@app.put("/todos/{id}")
def get_todo_id(title:str, id:int,db:Session=Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == id).first()

    todo.title = title

    db.commit()
    db.refresh(todo)
    
    return {"data":todo}

# DELETE
@app.delete("/todos/{id}")
def get_todo_id(id:int,db:Session=Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == id).first()

    db.delete(todo)
    db.commit()
    
    return {"data":todo}
