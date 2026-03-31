from fastapi import FastAPI
# from fastapi import Enum

# class ModelName(str, Enum):
    

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users")
async def read_users():
    return{"Alexis", "Jaja"}

@app.get("/users2")
async def read_users2():
    return{"Lexis", "Jao"}