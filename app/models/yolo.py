from ultralytics import YOLO
from app.models.detection import Detection


class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, image, domain):
        results = self.model(image)

        detections= []

        for result in results:
            boxes = result.boxes
            if boxes in None:
                continue

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                label = result.names[cls_id]

                crop = image.crop((x1, y1, x2, y2))

                detections.append(
                    Detection(
                        label=label,
                        confidence=conf,
                        bbox=[x1, y1, x2, y2],
                        crop=crop
                    )
                )
        return detections

yolo_model = YOLODetector()
