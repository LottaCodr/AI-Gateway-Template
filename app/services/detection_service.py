from app.models.yolo import yolo_model
from app.utils.image import load_image

def detect_items(image_url: str, domain: str):
    image = load_image(image_url)
    return yolo_model.detect(image, domain)
