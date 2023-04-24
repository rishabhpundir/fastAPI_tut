from fastapi import FastAPI ## importing the FastAPI class

app = FastAPI() ## Creating an instance (object) of the class

@app.get('/') ## adding a PATH, which is the route/url with the method attached to it
def index(): ## Path Operation Function
    return {"data": "Hello World!"} ## usually returned in a json/dictionary, although strings can go through also

@app.get('/about')
def index(): ## can have same path operation function names
    return {"data": {"value": "FastAPI"}}


## uvicorn main:app --reload