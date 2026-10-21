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

# {AREA}
class AreaBase(BaseModel):
    AREA:str

# - test -
class Item(BaseModel):
    name : str
    price : float
    in_stock : bool = True


# [ROUTES & CONTROLLERS]
# - [SALES] 
# {ITEM}
@app.post("/sales/items/", status_code=201)
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

@app.get("/sales/items/")
def items():
    return{
        "message" : "items()"
    }

# {AREA - POST}
@app.post("/sales/area", status_code=201)
def create_area(area:AreaBase,db:session = Depends(database.get_db)):
    # konversi data
    data_area = models.AreaModel(
        AREA=area.AREA
    )
    # Save db
    db.add(data_area)
    db.commit()
    db.refresh(data_area)

    return {
        "message" : "item registred succesfully",
        "data" : data_area
    }

# {AREA - GET}
@app.get("/sales/area", status_code=200)
def get_areas(db:session = Depends(database.get_db)):
    return{
        "msg" : "area is running"
    }
# - Testing -
@app.get("/")
def read_root():
    return {
        "status" : "oke",
        "status": "Engine is running smoothly"
    }