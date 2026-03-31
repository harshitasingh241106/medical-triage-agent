from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from environment import MedicalTriageEnv, Action

app = FastAPI(
    title="Medical Triage Agent",
    description="An OpenEnv environment where an AI agent triages patients to the correct department",
    version="1.0.0"
)

envs = {
    1: MedicalTriageEnv(task_number=1),
    2: MedicalTriageEnv(task_number=2),
    3: MedicalTriageEnv(task_number=3),
    4: MedicalTriageEnv(task_number=4)
}

class StepRequest(BaseModel):
    response: str
    task_number: int = 1

class ResetRequest(BaseModel):
    task_number: int = 1

@app.get("/")
def root():
    return {
        "name": "Medical Triage Agent",
        "version": "1.0.0",
        "status": "running",
        "endpoints": ["/reset", "/step", "/state", "/health", "/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/reset")
def reset(request: Optional[ResetRequest] = None):
    task_number = request.task_number if request else 1
    env = envs[task_number]
    obs = env.reset()
    return {
        "observation": obs.model_dump(),
        "status": "reset complete"
    }

@app.post("/step")
def step(request: StepRequest):
    env = envs[request.task_number]
    action = Action(response=request.response)
    try:
        obs, reward, done, info = env.step(action)
        return {
            "observation": obs.model_dump(),
            "reward": reward.model_dump(),
            "done": done,
            "info": info
        }
    except RuntimeError as e:
        return {"error": str(e), "hint": "Call /reset first"}

@app.get("/state")
def state(task_number: int = 1):
    env = envs[task_number]
    return env.state()

@app.get("/tasks")
def list_tasks():
    return {
        "tasks": [
            {"id": "task1", "name": "Department Routing", "difficulty": "easy", "description": "Route patient to correct department"},
            {"id": "task2", "name": "Department and Priority", "difficulty": "medium", "description": "Route patient and classify priority"},
            {"id": "task3", "name": "Full Triage", "difficulty": "hard", "description": "Route, priority, and recommend action"},
            {"id": "task4", "name": "Expert Triage Officer", "difficulty": "expert", "description": "Route, priority, risk flag, reasoning, and action"}
        ]
    }

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()