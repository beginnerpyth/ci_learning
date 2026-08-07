from fastapi import FastAPI,HTTPException
from fastapi.staticfiles import StaticFiles
import router_all
import uploadfile
app=FastAPI()
app.include_router(router_all.router)
app.include_router(uploadfile.router)
app.mount('/uploadfileurl',StaticFiles(directory='uploads'),name='anything')
@app.get('/')
def home():
    return 'You are home'
