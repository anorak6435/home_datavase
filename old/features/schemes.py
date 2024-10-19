# Feat: Scheme dataclasses
from dataclasses import dataclass
from typing import List
# Schemes
@dataclass
class ProgAttrib:
    name: str
    datatype: str

@dataclass
class ProgModel:
    name: str
    attribs : List[ProgAttrib]
