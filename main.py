from fastapi import FastAPI

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
