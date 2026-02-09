def classify_attributes(crop, domain):
    return {
        "color": color_model.predict(crop),
        "pattern": pattern_model.predict(crop)
    }