import requests
from PIL import Image
from io import BytesIO


def load_image(url: str):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))