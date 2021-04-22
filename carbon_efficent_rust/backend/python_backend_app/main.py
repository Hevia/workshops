from fastapi import FastAPI
#uvicorn main:app --reload
import time
from typing import Optional

app = FastAPI()

@app.get("/")
def main_route(name: Optional[str] = None):
    time.sleep(2)
    for i in range(100):
        if i == 50:
            print(50)
    return name
