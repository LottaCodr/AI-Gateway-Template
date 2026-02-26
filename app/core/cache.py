import hashlib
from functools import lur_cache

def generate_cache_key(image_url: str, domain: str):
    key = f"{image_url}:{domain}"
    return hashlib.md5(key.encode()).hexdigest()