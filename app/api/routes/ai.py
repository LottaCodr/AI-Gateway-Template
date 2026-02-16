from fastapi import APIRouter
from app.api.schemas import VisionRequest
from app.services.ai_orchestrator import process_item

router = APIRouter()

@router.post("/process-item")
def process(req: VisionRequest):
    return process_item(req.image_url, req.domain)