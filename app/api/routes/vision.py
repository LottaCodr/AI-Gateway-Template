from fastapi import APIRouter
from app.api.schemas import VisionRequest, VisionResponse
from app.pipelines.vision_pipeline import run_pipeline

router = APIRouter()

@router.post("/analyze", response_model=VisionResponse)
def analyze(req: VisionRequest):
    return run_pipeline(req.image_url, req.doman)

    