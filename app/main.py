from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Wall Damage Detector")
app.include_router(router)