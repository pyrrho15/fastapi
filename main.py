from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI();

@app.get("/")
def home():
    return {"msg":"helloowwwwwww"}

# path parameters
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}

#query parameters
@app.get("/users")
def get_user(name:str ="rohit"):
    return {"name":name}
# multiple query parameters
@app.get("/item")
def get_user(name:str ="Brush", price:int=90):
    return {"name":name, "price":price}

# post request

@app.post("/create-user")
def create_user(name:str, age:int):
    return {
        "success":"true",
        "message":f'hello {name}, your age is {age}'
    }

@app.post("/create-user-dict")
def create_user_dict(details:dict):
    return {
        "success":"true",
        "data":details
    }

# use pydanic for data validation
#  below is schema
class User(BaseModel):
    name:str
    age:int
    address:str
@app.post("/create-user-pydantic")
def create_user_dict(details:User):
    return {
        "success":"true",
        "data":details
    }
# below is nested schema
class Address(BaseModel):
    city:str
    pincode:int
class User(BaseModel):
    name:str
    age:int
    address:Address
@app.post("/create-user-nest")
def create_user_dict(details:User):
    return {
        "success":"true",
        "data":details
    }


# simple todo app
todos = []
class Todo(BaseModel):
    id:int
    title:str
    isCompleted:bool

@app.post("/create_todo")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"todo created"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todo/{id}")
def get_todos(id:int):
    for todo in todos:
        if todo.id == id:
            return todo
    return {"error":"todo not found"}

@app.put("/todo/{id}")
def update_todo(id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated_todo
            return {"msg":"updated", "data":updated_todo}
        else:
            return {"error":"todo not found"}

@app.delete("/todo/{id}")
def delete_todo(id:int):
    for index,todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
            return {"msg":"deleted"}
        else:
            return {"error":"todo not found"}


# Connect sqliteDB
conn = sqlite3.connect("test.db", check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
)
""")
conn.commit()

@app.get("/")
def home():
    return{
        "message": "SQLite Connected fine"
    }