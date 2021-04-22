from fastapi import Body, Request, FastAPI
from pydantic import BaseModel



# init our API
app = FastAPI()

# init our data models
class SearchData(BaseModel):
    search_query: str

# You can use this to test if the server is alive
@app.get("/")
def ping():
    return {"Hello": "World"}


@app.post("/search")
def search(searchData: SearchData):
    search_query = searchData.search_query
    search_results = ["We found something!"]

    return {"search_results": search_results}