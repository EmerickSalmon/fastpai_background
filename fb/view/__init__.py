from fastapi import FastAPI, BackgroundTasks
from fb.controler import create_order, manage_tasks, task_status

app = FastAPI()

@app.get("/health/")
def health():
    return "Up"

@app.post("/task/")
def l_task(background_tasks: BackgroundTasks, id:str, delay:int = 5):
    create_order(id)
    background_tasks.add_task(manage_tasks, id)
    return {"Result": "finished"}

@app.get("/task/")
def t_status(id:str):
    return {'status': task_status(id)}