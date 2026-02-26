from pydantic import BaseModel
from typing import Dict, List, Optional


class VisionRequest(BaseModel):
    image_url: str
    domain: str #fashion | space | garden

class VisionItem(BaseModel):
    category: str
    attributes: Dict
    style_tags: List[str]
    embedding_id: str
    bounding_box: List[float]
    confidence: float

class VisionResponse(BaseModel):
    image_url: str
    items: List[VisionItem]
    