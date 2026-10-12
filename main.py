from fastapi import FastAPI
from pydantic import BaseModel

# Endpoint
app = FastAPI(title="simple-API", version="1.0.0")

# validation
class Item(BaseModel):
    name : str
    price : float
    in_stock : bool = True

# - testing validation -
@app.post("/items/")
def create_item(item:Item):
    return {
        "message" : "item registred succesfully",
        "data" : item
    }


# - Testing -
@app.get("/")
def read_root():
    return {
        "status" : "oke",
        "status": "Engine is running smoothly"
    }