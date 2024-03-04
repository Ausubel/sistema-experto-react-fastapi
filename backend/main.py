from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def get_question():
    return {"Hello": "World"}

@app.post("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}