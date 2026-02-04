from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "Muhammad!"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q" : q}