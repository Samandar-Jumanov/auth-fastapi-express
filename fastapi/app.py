from fastapi import FastAPI
app = FastAPI()
import models 
from database import engine 
import users_route
models.Base.metadata.create_all(engine)
import posts


@app.get('/')
def hello():
    return 'Hello world '
 

app.include_router(users_route.router)
app.include_router(posts.router)


 