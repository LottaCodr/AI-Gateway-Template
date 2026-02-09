import torch
import open_clip


class CLIPModel:
    def __init__(self) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name="ViT-B-32",
            pretrained="openai"
        )

        self.model = self.model.to(self.device)
        self.model.eval()

        self.tokenizer = open_clip.get_tokenizer("ViT-B-32")

    def embed_image(self, image):
        """
        image: PIL.Image
        """
        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            features = self.model.encode_image(image_tensor)

        return features.cpu().tolist()

    def embed_text(self, texts):
        """
        texts: List[str]
        """
        text_tokens = self.tokenizer(texts).to(self.device)

        with torch.no_grad():
            features = self.model.encode_text(text_tokens)

        return features.cpu().tolist()

    def predict_styles(self, image):
        styles = ["casual", "formal", "streetwear", "minimal"]

        image_features = self.embed_image(image)
        # Placeholder logic for now
        return styles[:2]


clip_model = CLIPModel()
