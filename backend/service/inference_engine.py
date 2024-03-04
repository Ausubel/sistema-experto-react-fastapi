from typing import List
from models.knowledge_base_repository import KnowledgeBase
from entities.entry import Entry
from entities.property import Property
from entities.response import Response

class InferenceEngine:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.accepted_responses: List[Response] = []
        self.rejected_responses: List[Response] = []
        self.respose: Response = Response.NO
        self.result: Entry or None = None # type: ignore
    
    def process(self):
        self.accepted_responses: List[Property] = []
        self.rejected_responses: List[Property] = []
        
        for entry in self.knowledge_base.entries:
            correct_entry = True
            if not self._check_rule_2(entry) and not self._check_rule_3(entry):
                continue
            for prop in entry.properties:
                if not self._check_rule_1(prop):
                    continue
                yield prop
                
                if self.response == Response.YES:
                    self.accepted_responses.append(prop)
                else:
                    self.rejected_responses.append(prop)
                    correct_entry = False
                    break
            if correct_entry:
                self.result = entry
                yield None
        self.result = None
        yield None
                
            
    def set_response(self, response: Response):
        self.response = response

    def _check_rule_1(self, prop: Property) -> bool:

        return (prop not in self.accepted_properties and
                prop not in self.denied_properties)

    def _check_rule_2(self, entry: Entry) -> bool:

        for prop in self.accepted_properties:
            if prop not in entry.properties:
                return False
        return True

    def _check_rule_3(self, entry: Entry) -> bool:

        for prop in self.denied_properties:
            if prop in entry.properties:
                return False
        return True