from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory storage for tasks
items = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]


class ItemCreate(BaseModel):
    title: str
    done: bool = False


class ItemUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API!"}


@app.get("/items")
def get_items():
    # TODO: return all items from the in-memory list
    return items


@app.post("/items")
def create_item(item: ItemCreate):
    # TODO: create a new item with a unique id and append it to the list
    # HINT: item.title should be stored, and item.done should be respected
    new_item = {"id": len(items) + 1, "title": item.title, "done": item.done}
    items.append(new_item)
    return new_item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: find the item by id and return it
    # TODO: raise HTTPException(status_code=404, detail="Item not found") if missing
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    # TODO: update the item if it exists
    # TODO: raise HTTPException(status_code=404, detail="Item not found") if missing
    for index, current in enumerate(items):
        if current["id"] == item_id:
            if item.title is not None:
                current["title"] = item.title
            if item.done is not None:
                current["done"] = item.done
            return current
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: remove the item from the list and return a success message
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(index)
            return {"message": f"Deleted item {item_id}", "deleted": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
