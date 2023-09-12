from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    brand: str = None


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inventory = {1: {"name": "Milk", "price": 3.99, "brand": "Regular"}}


@app.get("/")
def home():
    return {"data:" "test"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory.get(item_id)


@app.get("/get-by-name")
def get_by_name(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        else:
            return {"data": "not found"}


@app.get("/get-all")
def get_all():
    return inventory


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "item_id taken"}
    else:
        inventory[item_id] = item
        return {"Response": "success"}
