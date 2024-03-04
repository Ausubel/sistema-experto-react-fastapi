from service.inference_engine import InferenceEngine

class ApiServices():
    def __init__(self, inference_engine: InferenceEngine):
        self.inference_engine: InferenceEngine = inference_engine
        self.questions = self.inference_engine.process()
    
    def get_question_service(self):
        try:
            next_question = next(self.questions)
            if next_question is None:
                return self._finished()
            return next_question
        except StopIteration:
            return self._finished()
        
    def _finished(self):
        if self.inference_engine.result is None:
            return {"Error": "No result found"}
        return self.inference_engine.result