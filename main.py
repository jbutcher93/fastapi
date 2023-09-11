from fastapi import FastAPI

app = FastAPI()

inventory = {1: {"name": "Milk", "price": 3.99, "brand": "Regular"}}


@app.get("/")
def home():
    return {"data:" "test"}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory.get(item_id)
