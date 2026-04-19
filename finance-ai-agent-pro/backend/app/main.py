from fastapi import FastAPI 
from app.routes import router 
app = FastAPI(title="Finance AI Agent") 
app.include_router(router) 
