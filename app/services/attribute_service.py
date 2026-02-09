from app.models.attributes.color import color_model
from app.models.attributes.pattern import pattern_model


def classify_attributes(crop, domain):
    return {
        "color": color_model.predict(crop),
        "pattern": pattern_model.predict(crop)
    }