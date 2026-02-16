from app.pipelines.vision_pipeline import run_pipeline
from app.services.llm_service import enhance_with_llm

def process_item(image_url: str, domain: str):
    """
    High-level AI orchestration:
    Vision -> LLM -> Aggregation 
    """


    #step 1: Vision analysis
    vision_result = run_pipeline(image_url, domain)

    #step 2: Enhance with llm reasoning
    enhance_result = enhance_with_llm(vision_result)


    return enhance_result