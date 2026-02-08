from pydantic import BaseModel
from typing import List, Optional

class ImageInput(BaseModel):
    image_url: str

class VisionRequest(BaseModel):
    images: List[ImageInput]
    task: Optional[str]= "full"

class DetectedItem(BaseModel):
    label: str
    confidence: float
    bbox: List[int]

class VisionResponse(BaseModel):
    items: List[DetectedItem]