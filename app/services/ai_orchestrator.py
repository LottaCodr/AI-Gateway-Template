from app.pipelines.vision_pipeline import run_pipeline
from app.services.llm_service import enhance_with_llm
from app.core.cache import generate_cache_key

__cache = {}

def process_item(image_url: str, domain: str):
    """
    High-level AI orchestration:
    Vision -> LLM -> Aggregation 
    """

    cache_key = generate_cache_key(image_url, domain)

    if cache_key in __cache:
        return __cache[cache_key]


    #step 1: Vision analysis
    vision_result = run_pipeline(image_url, domain)

    #step 2: Enhance with llm reasoning
    enhanced_result = enhance_with_llm(vision_result)

    __cache[cache_key] = enhanced_result


    return enhanced_result