from fastapi import FastAPI, BackgroundTasks
from fb.controler import long_task

app = FastAPI()

@app.get("/health/")
def health():
    return "Up"

@app.post("/long-task/")
def l_task(background_tasks: BackgroundTasks, delay:int = 5):
    background_tasks.add_task(long_task, delay)
    return {"Result": "finished"}