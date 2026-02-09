import numpy as np
from PIL import Image


class ColorModel:
    """
    Simple color inference model.
    This is a placeholder that can later be replaced
    with a trained classifier.
    """

    def predict(self, image: Image.Image) -> str:
        image = image.resize((50, 50))
        pixels = np.array(image)

        avg_color = pixels.mean(axis=(0, 1))  # RGB mean
        r, g, b = avg_color

        if r > g and r > b:
            return "red"

        if g > r and g > b:
            return "green"

        if b > r and b > g:
            return "blue"

        return "neutral"

color_model = ColorModel()