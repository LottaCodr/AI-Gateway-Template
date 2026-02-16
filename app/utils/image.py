import requests
from PIL import Image
from io import BytesIO


def load_image(url: str):
    try:
        response = requests.get(url,  timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to download image: { str(e)}")

    try:
        return Image.open(BytesIO(response.content)).convert("RGB")
    except Exception:
        raise ValueError("Download file is not valid image")
    #response = requests.get(url)