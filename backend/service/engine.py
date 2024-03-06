from typing import List
from repository.knowledge_base_repository import KnowledgeBase
from entities.entry import Entry
from entities.property import Property
from entities.response import Response

class Inference:
    def __init__(self, path: str):
        self.path = path
        self.knowledge_base = KnowledgeBase(self.path)
        self.accepted_properties: List[Response] = []
        self.rejected_properties: List[Response] = []
        self.response: Response = Response.YES
        self.result: Entry or None = None # type: ignore
    
    def process(self):
        self.accepted_properties: List[Property] = []
        self.rejected_properties: List[Property] = []
        self.result = None
        for entry in self.knowledge_base.entries:
            correct_entry = True
            if not self._has_all_required_properties(entry):
                continue
            if not self._has_no_excluded_properties(entry):
                continue
            for prop in entry.properties:
                if self._is_property_asked(prop):
                    continue
                
                yield prop
                
                if self.response == Response.YES:
                    self.accepted_properties.append(prop)
                else:
                    self.rejected_properties.append(prop)
                    correct_entry = False
                    break
                
                
            if correct_entry:
                self.result = entry
                for prop in self.accepted_properties:
                    print(f"Accepted: {prop.name}")
                for prop in self.rejected_properties:
                    print(f"Rejected: {prop.name}")
                yield None
        yield None
                
            
    def set_response(self, response: Response):
        self.response = response
    
    def get_response(self) -> Response:
        return self.response

    def _is_property_asked(self, prop: Property) -> bool:
        return prop in (self.accepted_properties + self.rejected_properties)

    def _has_all_required_properties(self, entry: Entry) -> bool:
        for prop in self.accepted_properties:
            if prop not in entry.properties:
                return False
        print("All required properties are present")
        for prop in entry.properties:
            print(f"Entry has: {prop.name}")
        for prop in self.accepted_properties:
            print(f"Required: {prop.name}")
        return True


    def _has_no_excluded_properties(self, entry: Entry) -> bool:
        print("Checking for excluded properties")
        for prop in self.rejected_properties:
            print(f"Excluded: {prop.name}")
            if prop in entry.properties:
                print(f"Excluded property {prop.name} is present")
                return False
        print("No excluded properties are present")
        return True
    
    def reset(self):
        self.accepted_properties = []
        self.rejected_properties = []
        self.response = Response.YES
        self.result = None
        self.knowledge_base = KnowledgeBase(self.path)