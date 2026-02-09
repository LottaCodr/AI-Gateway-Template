from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, image, domain):
        results = self.model(image)
        return results

yolo_model = YOLODetector()
