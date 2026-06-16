from fastapi import FastAPI
from agents.coordinator import CoordinatorAgent

app = FastAPI()

coordinator = CoordinatorAgent()


@app.get("/")
def home():
    return {
        "message": "Welcome to VoyagerAI"
    }


@app.post("/plan-trip")
def plan_trip(data: dict):

    result = coordinator.process_request(data)

    return result