from typing import List
from repository.knowledge_base_repository import KnowledgeBase
from entities.entry import Entry
from entities.property import Property
from entities.response import Response

class InferenceEngine:
    def __init__(self, path: str):
        self.knowledge_base = KnowledgeBase(path)
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
            if not self._check_rule_2(entry) and not self._check_rule_3(entry):
                continue
            for prop in entry.properties:
                if not self._check_rule_1(prop):
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
                yield None
        yield None
                
            
    def set_response(self, response: Response):
        self.response = response
    
    def get_response(self) -> Response:
        return self.response

    def _check_rule_1(self, prop: Property) -> bool:

        return (prop not in self.accepted_properties and
                prop not in self.rejected_properties)

    def _check_rule_2(self, entry: Entry) -> bool:

        for prop in self.accepted_properties:
            if prop not in entry.properties:
                return False
        return True

    def _check_rule_3(self, entry: Entry) -> bool:

        for prop in self.rejected_properties:
            if prop in entry.properties:
                return False
        return True