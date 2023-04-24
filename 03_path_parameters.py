from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": "Blog List"}

#2
@app.get('/blog/{id}') ## adding a variable to the route
def show(id):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

@app.get('/blog/{id}/type')
def var_type(id: int): ## explicitly declaring the datatype of the variable
    return {'data': {f"{id}": f"{type(id)}"}}

@app.get('/blog/unpub') 
## This one can clash with #2 if #2 id is declared int, 
## as fast api will match the routes from top to bottom one by one
## and whatever path matches the criteria first will be executed,
## so the best practice is to keep the dynamic paths lower in the 
## hierarchy of the file.
def unpub_blogs():
    return {'data': 'all unpublished blogs'}