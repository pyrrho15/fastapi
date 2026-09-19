from fastapi import FastAPI
from pydantic import BaseModel

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

