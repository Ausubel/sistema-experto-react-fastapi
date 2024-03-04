from service.inference_engine import InferenceEngine

class ApiServices():
    def __init__(self, inference_engine: InferenceEngine):
        self.inference_engine: InferenceEngine = inference_engine
        self.questions = self.inference_engine.process()
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
        if self.inference_engine.result is None:
            return {"Error": "No result found"}
        return self.inference_engine.result
    def reset(self):
        self.inference_engine.reset()
        self.questions = self.inference_engine.process()
        self.canAsk = True