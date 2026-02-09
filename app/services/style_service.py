from app.models.clip_model import clip_model


def infer_style(crop):
    return clip_model.predict_styles(crop)