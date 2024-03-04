from fastapi import FastAPI
from service.inference_engine import InferenceEngine
from service.api_services import ApiServices
from entities.response import Response

app = FastAPI()

inference_engine = InferenceEngine("./data/knowledge_base.json")

api_services = ApiServices(inference_engine)

@app.post("/{response}")
def get_question(response: int):
    allowed_responses = [Response.YES.value, Response.NO.value]
    if response not in allowed_responses:
        return {"Error": "Invalid response. Input should be 1 or 0"}
    inference_engine.set_response(Response(response))
    print(inference_engine.get_response())
    return api_services.get_question_service()
