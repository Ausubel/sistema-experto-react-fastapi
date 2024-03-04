from typing import List
from backend.entities.entry import Entry
from io import open
import json
from utils import singleton


@singleton
class KnowledgeBase:
    def __init__(self):
        self.entries: List[Entry] = []
        self.description: str
        self.read_from_json("../data/knowledge_base.json")
        
    def read_from_json(self, file_path: str):
        with open(file_path, "r", encoding='utf8') as file:
            data = file.read()
            
        json_data = json.loads(data)
        
        self.description = json_data["description"]
        
        for json_entry in json_data["entries"]:
            entry: Entry = self.get_or_add_entry(str(json_entry["name"]))
            entry.description = str(json_entry["description"])
            for json_prop in json_entry["props"]:
                entry.get_or_add_prop(str(json_prop))
        return self
            

    def get_or_add_entry(self, name: str) -> Entry:
        for entry in self.entries:
            if entry.is_equal(name):
                return entry
        entry = Entry(name)
        self.entries.append(entry)
        return entry
    
    def __str__(self):
        res = f"[{self.description}]"
        for entry in self.entries:
            res += f"\n{entry}\n"
        return res