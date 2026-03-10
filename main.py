from fastapi import FastAPI  
from app.api.routes.vision import router as vision_router
from app.api.routes.ai import router as ai_router


app = FastAPI(
    title="Glimms Vision Service",
    version="0.1.0",
    description="Computer Vision service for clothing, style, and environment analysis"
)

app.include_router(vision_router, prefix="/vision", tags=["Vision"])
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def root():
    return {"service": "Glimms AI Gateway", "status": "running"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "vision",
    }

