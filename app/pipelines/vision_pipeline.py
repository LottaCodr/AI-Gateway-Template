from app.services.detection_service import detect_items
from app.services.attribute_service import classify_attributes
from app.services.style_service import infer_style
from app.services.embedding_service import generate_embedding


def run_pipeline(image_url: str, domain: str):
    detections = detect_items(image_url, domain)

    items = []
    for det in detections:
        attributes = classify_attributes(det.crop, domain)
        style_tags =  infer_style(det.crop)
        embedding_id = generate_embedding(det.crop)

        items.append({
            "category": det.label,
            "attributes": attributes,
            "style_tags": style_tags,
            "bounding_box": det.bbox,
            "confidence" : det.confidence,
            "embedding_id": embedding_id
        })

    return {
        "image_url": image_url,
        "items": items
    }