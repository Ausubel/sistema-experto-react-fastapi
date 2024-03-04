from pydantic import BaseModel
from typing import List
from .property import Property

class Entry(BaseModel):
    name: str
    description: str
    price: str
    url: str
    properties: List[str]
    
    def get_or_add_prop(self, name: str) -> Property:
        for prop in self.properties:
            if prop.is_equal(name):
                return prop
        prop = Property(name)
        self.properties.append(prop)
        return prop
            
    def is_equal(self, name: str) -> bool:
        return self.name.lower() == name.lower().strip()