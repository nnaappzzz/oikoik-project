from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session
from pydantic import BaseModel
from typing import List

import models
import database

# [INITIALIZE]
# - Gen. tabel otomatis -
models.Base.metadata.create_all(bind = database.engine)
# Endpoint
app = FastAPI(title="simple-API", version="1.0.0")

#  [VALIDATION]
class SaleCreate(BaseModel):
    item_name: str
    quantity:int
    total_price:float

class SaleResponse(SaleCreate):
    id: int
    created_at: str

    class Config:
        orm_mode = True

# - test -
class Item(BaseModel):
    name : str
    price : float
    in_stock : bool = True


# [ROUTES]
# - [SALES] ITEM
@app.post("/items/", status_code=201)
def create_item(item:Item,db:session = Depends(database.get_db)):
    # Konversi data sales
    data_sales = models.SalesModel(
        item_name = item.name,
        total_price= item.price,
       quantity=item.in_stock
    )
    # Simpan ke SQLITE
    db.add(data_sales)
    db.commit()
    db.refresh(data_sales)
    return {
        "message" : "item registred succesfully",
        "data" : item
    }

@app.get("/items/")
def items():
    return{
        "message" : "items()"
    }

# - Testing -
@app.get("/")
def read_root():
    return {
        "status" : "oke",
        "status": "Engine is running smoothly"
    }