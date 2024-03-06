from service.engine import Inference

class ApiServices():
    def __init__(self, engine: Inference):
        self.engine: Inference = engine
        self.questions = self.engine.process()
        self.canAsk = True
    
    def get_question_service(self):
        if not self.canAsk:
            return self._finished()
        try:
            next_question = next(self.questions)
            if next_question is None:
                print("No more questions")
                return self._finished()
            return next_question
        except StopIteration:
            print("No more questions StopIteration  ")
            return self._finished()
    
    def _finished(self):
        self.canAsk = False
        if self.engine.result is None:
            return {"Error": "No result found"}
        return self.engine.result
    def reset(self):
        self.engine.reset()
        self.questions = self.engine.process()
        self.canAsk = True