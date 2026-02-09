class PatternModel:
    """
    Placeholder pattern classifier.
    Can be replaced with a CNN or ViT later.
    """

    def predict(self, image) -> str:
        # Temporary heuristic
        # Later: texture analysis or trained model

        return "solid"

pattern_model = PatternModel()