def enhance_with_llm(vision_result: dict) -> dict:
    """
    Simulated LLM reasoning layer.
    Later this will call Open AI/Local model
    """

    items = vision_result.get("items", [])

    for item in items:
        item["style_summary"] = generate_style_summary(item)
    
    vision_result["summary"] = generate_overall_summary(items)

    return vision_result


def generate_style_summary(item: dict) -> str:
    return f"This {item['category']} has a {item['attributes'].get('color')} tone and fits a modern aesthetic"

def generate_overall_summary(items: list) -> str:
    return f"Detected {len(items)} items with cohesive style characteristics."