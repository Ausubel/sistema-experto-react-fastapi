from typing import List
from .property import Property

class Entry():
    name: str
    description: str
    price: str
    url: str
    properties: List[str]
    
    def __init__(self, name: str):
        self.name = name
        self.description = ""
        self.properties = []
        self.price = ""
        self.url = ""
    
    def get_or_add_prop(self, name: str) -> Property:
        for prop in self.properties:
            if prop.is_equal(name):
                return prop
        prop = Property(name)
        self.properties.append(prop)
        return prop
            
    def is_equal(self, name: str) -> bool:
        return self.name.lower() == name.lower().strip()