from bson import ObjectId
from pydantic import BaseModel
from typing import Optional, List

# MongoDB Snippet Model
class SnippetInDB(BaseModel):
    id: Optional[str] = None  # MongoDB's ObjectId will be stored as a string
    title: str
    description: Optional[str] = None
    code: Optional[str] = None
    tags: List[str] = []
    links: List[str] = []

    class Config:
        orm_mode = True

# Utility function to convert MongoDB item (dict) to Pydantic Item
def snippet_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "code": item["code"],
        "tags": item["tags"],
        "links": item["links"]
    }