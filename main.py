from pydantic import BaseModel ## All the request models are defined through pydantic baseModel
from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()
class Blog(BaseModel): ## Creating a POST request body for the user to fill data in
    title: str
    body: str ## Anything not optional will be marked as required in the request
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog): 
    ## Here the request body is not an inherent object of the framework
    ## but rather used through the user defined request model.
    return {'data': f"The title is : '{request.title}'."}

if __name__ == '__main__':
    uvicorn.run(app, port=9000)