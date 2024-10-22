from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Snippet():
    id: Optional[str]  # MongoDB's ObjectId will be stored as a string
    title: str
    description: Optional[str] = None
    code: Optional[str] = None
    tags: List[str] = None
    links: List[str] = None