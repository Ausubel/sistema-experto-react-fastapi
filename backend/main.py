from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from service.inference_engine import InferenceEngine
from service.api_services import ApiServices
from entities.response import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
inference_engine = InferenceEngine("./data/knowledge_base.json")

api_services = ApiServices(inference_engine)

@app.post("/response/{response_value}")
def get_question(response_value: int):
    allowed_responses = {Response.YES.value, Response.NO.value}
    
    if response_value not in allowed_responses:
        raise HTTPException(status_code=400, detail="Invalid response. Input should be 0 or 2")

    try:
        inference_engine.set_response(Response(response_value))
        return HTTPException(status_code=200, detail=api_services.get_question_service())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/start")
def start_session():
    try:
        api_services.reset()
        return HTTPException(status_code=200, detail=api_services.get_question_service())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))