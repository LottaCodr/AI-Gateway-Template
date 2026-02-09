from fastapi import APIRouter
from app.api.schemas import VisionRequest, VisionResponse

router = APIRouter()

@router.post("/analyze", response_model=VisionResponse)
async def analyze_images(payload: VisionRequest):
    # Temporary stub (no ML yet)
    return {
        "items": [
            {
                "label": "shirt",
                "confidence": 0.98,
                "bbox": [10,20,200, 300]
            }
        ]
    }

    