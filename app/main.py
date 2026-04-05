from fastapi import FastAPI

from app.core.logger import get_logger
from app.api.routes import router

log = get_logger()

app = FastAPI(
    title="Customer Feedback AI System",
    version="1.0"
)

@app.on_event("startup")
def startup_event():
    log.info("Feedback AI System Started")

@app.get("/")
def root():
    return {"message": "API running"}

# include API routes
app.include_router(router)