from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
