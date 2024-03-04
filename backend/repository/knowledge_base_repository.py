from typing import List
from entities.entry import Entry
from io import open
import json
from utils.singleton_decorator import singleton


@singleton
class KnowledgeBase:
    def __init__(self, path: str):
        self.entries: List[Entry] = []
        self.description: str
        self.read_from_json(path)
        
    def read_from_json(self, file_path: str):
        with open(file_path, "r", encoding='utf8') as file:
            data = file.read()
            
        json_data = json.loads(data)
        
        self.description = json_data["description"]
        
        for json_entry in json_data["entries"]:
            entry: Entry = self.get_or_add_entry(str(json_entry["name"]))
            entry.description = str(json_entry["description"])
            entry.price = str(json_entry["price"])
            entry.url = str(json_entry["url"])
            for json_prop in json_entry["props"]:
                entry.get_or_add_prop(str(json_prop))
        return self
            

    def get_or_add_entry(self, name: str) -> Entry:
        for entry in self.entries:
            if entry.is_equal(name):
                return entry
        new_entry = Entry(name)
        self.entries.append(new_entry)
        return new_entry
    
    def __str__(self):
        res = f"[{self.description}]"
        for entry in self.entries:
            res += f"\n{entry}\n"
        return res