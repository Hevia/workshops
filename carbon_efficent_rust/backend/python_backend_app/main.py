from fastapi import FastAPI
#uvicorn main:app --reload
import time
from typing import Optional

app = FastAPI()

@app.get("/")
def main_route(name: Optional[str] = None):
    time.sleep(2)
    for i in rang
    return name
