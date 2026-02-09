import clip
import torch

class CLIPModel:
    def __init__(self) -> None:
        self.model, self.preprocess = clip.load("ViT-B/32")

        
    def embed(self, image):
        return self.model.encode_image(image).cpu().tolist()

    def predict_styles(Self, image):
        styles = ["casual", "formal", "streetwear", "minimal"]
        return styles[:2]

clip_model = CLIPModel()