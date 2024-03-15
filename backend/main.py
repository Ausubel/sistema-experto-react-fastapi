from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from service.engine import Engine
from service.api_services import ApiServices
from entities.response import Response

app = FastAPI()
app = FastAPI(title="SE - AIFindy", version="1.0", description="Sistema experto en recomendacion de herramientas de inteligencia artificial en base a la web AIFindy.")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
engine = Engine("./data/knowledge_base_full_stack_web.json")

api_services = ApiServices(engine)

@app.get("/start", tags=["Start session"])
def start_session():
    try:
        api_services.reset()
        return HTTPException(status_code=200, detail=api_services.get_question_service())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/response/{response_value}", tags=["Response to question"])
def get_question(response_value: int):
    allowed_responses = {Response.YES.value, Response.NO.value}
    
    if response_value not in allowed_responses:
        raise HTTPException(status_code=400, detail="Invalid response. Input should be 0 or 2")

    try:
        engine.set_response(Response(response_value))
        return HTTPException(status_code=200, detail=api_services.get_question_service())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
