from fastapi import FastAPI
from fb.controler import long_task

app = FastAPI()

@app.get("/health/")
def health():
    return "Up"

@app.port("/long-task/")
def l_task(delay:int = 5):
    long_task(delay)
    return {"Result": "finished"}