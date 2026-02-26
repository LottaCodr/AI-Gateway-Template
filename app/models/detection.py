from dataclasses import dataclass
from typing import List
from PIL import Image


@dataclass
class Detection:
    label: str
    confidence: float
    bbox: List[float]
    crop: Image.Image
