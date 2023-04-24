from fastapi import FastAPI
from typing import Optional ## is used to declare optional parameters through the path operations

app = FastAPI()

@app.get('/blog')
def show(limit=10, pub=False, sort: Optional[str] = None): ## adding query parameters
    return {'data': f'max {limit} blog limit and Published = {pub}. Sort keyword is {sort}.'}
