## Glimms AI Gateway – Vision Service

This project is a **FastAPI-based microservice** that provides computer vision and AI capabilities for analyzing images of **fashion, spaces, and gardens**.  
It detects items in an image, classifies visual attributes, infers style tags, and generates vector embeddings that can be used by downstream recommendation or search systems.

### Features

- **REST API with FastAPI**
  - Root (`/`) and `/health` endpoints for basic status checks.
  - `/vision/analyze` endpoint for computer vision analysis.
  - `/ai/process-item` endpoint for AI/LLM-style processing of detected content.
- **Vision pipeline**
  - Object detection using YOLOv8 (`yolov8n.pt`).
  - Attribute classification (e.g., color, material, pattern) for fashion/space/garden domains.
  - Style inference and tag generation.
  - Embedding generation for each detected item.
- **Modular architecture**
  - `app/api` – FastAPI routers and request/response schemas.
  - `app/pipelines` – High-level vision pipelines.
  - `app/services` – Detection, attribute, style, embedding, and AI orchestration services.
  - `app/models` – Model loading and helper utilities (YOLO, CLIP, attribute models, etc.).
  - `app/core` – Configuration, caching, and vector store utilities.
  - `app/utils` – Image utilities (downloading, preprocessing, cropping).

---

### Project Structure

Key directories and files:

- `app/main.py` – FastAPI app definition and router registration.
- `app/api/routes/vision.py` – Vision analysis endpoints.
- `app/api/routes/ai.py` – AI orchestration endpoints.
- `app/api/schemas.py` – Pydantic models for requests/responses.
- `app/pipelines/vision_pipeline.py` – Orchestrates detection, attributes, style, and embeddings.
- `app/services/*` – Core business logic for individual services.
- `app/models/*` – Model wrappers and attribute taxonomies.
- `yolov8n.pt` – YOLOv8 model weights (small variant).

---

### Requirements

Python **3.10+** is recommended.

Runtime dependencies are captured in `requirements.txt`:

- FastAPI / Uvicorn
- PyTorch / TorchVision
- Ultralytics (YOLOv8)
- OpenCV
- Pillow
- CLIP (via `clip-anytorch`)
- Pydantic, NumPy, python-dotenv, etc.

You will also need a compatible **CUDA** setup if you intend to run models on GPU; otherwise the service can run on CPU (slower).

---

### Setup

1. **Clone the repository**

```bash
git clone <your-repo-url> ai-gateway
cd ai-gateway
```

2. **(Optional) Create and activate a virtual environment**

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows PowerShell
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Environment configuration (optional but recommended)**

Create a `.env` file in the project root if you need to configure:

- Model paths or cache directories
- Vector store or database URLs
- External service endpoints or API keys

See `app/core/config.py` for available configuration options.

---

### Running the Service

From the project root:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- Base URL: `http://localhost:8000`
- Interactive docs (Swagger UI): `http://localhost:8000/docs`
- Alternative docs (ReDoc): `http://localhost:8000/redoc`

Health check:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "vision"
}
```

---

### API Overview

#### Root

- **GET** `/`
- **Response**:

```json
{
  "service": "Glimms AI Gateway",
  "status": "running"
}
```

---

#### Vision – Analyze Image

- **Endpoint**: `POST /vision/analyze`
- **Description**: Runs the full vision pipeline on an input image URL for a specific domain (e.g., fashion, space, garden).
- **Request body** (`VisionRequest`):

```json
{
  "image_url": "https://example.com/image.jpg",
  "domain": "fashion"
}
```

- **Response** (`VisionResponse`):

```json
{
  "image_url": "https://example.com/image.jpg",
  "items": [
    {
      "category": "dress",
      "attributes": {
        "color": "red",
        "pattern": "floral"
      },
      "style_tags": ["boho", "summer"],
      "embedding_id": "emb_123456",
      "bounding_box": [x_min, y_min, x_max, y_max],
      "confidence": 0.94
    }
  ]
}
```

> Note: The exact attribute keys and style tags depend on your attribute and style models.

---

#### AI – Process Item

- **Endpoint**: `POST /ai/process-item`
- **Description**: Higher-level AI/LLM-oriented processing over the provided image and domain (e.g., generating descriptions or recommendations). Internally calls `app.services.ai_orchestrator.process_item`.
- **Request body** (`VisionRequest`):

```json
{
  "image_url": "https://example.com/image.jpg",
  "domain": "fashion"
}
```

- **Response**: Arbitrary JSON depending on your orchestration logic, e.g.:

```json
{
  "summary": "A red floral summer dress styled for a casual outing.",
  "style_insights": [...],
  "recommendations": [...]
}
```

Check `app/services/ai_orchestrator.py` for the exact response structure.

---

### Vision Pipeline Details

The core vision pipeline is implemented in `app/pipelines/vision_pipeline.py` and is roughly:

1. **Detection** – `detect_items(image_url, domain)`  
2. **Attribute classification** – `classify_attributes(det.crop, domain)`  
3. **Style inference** – `infer_style(det.crop)`  
4. **Embedding generation** – `generate_embedding(det.crop)`  

It returns a structured payload with per-item metadata (category, attributes, style tags, embedding ID, bounding box, confidence).

---

### Model Weights

- The repository includes `yolov8n.pt` as the default detection model.
- Other models (e.g., CLIP, attribute classifiers) may be downloaded automatically on first run (depending on implementation) or configured via environment variables / config.

If you prefer to use a different YOLO model (e.g., `yolov8s.pt`), adjust the corresponding configuration or model-loading code in `app/models/yolo.py`.

---

### Development Notes

- **Code style**: The project uses FastAPI with standard Python packaging conventions.
- **Hot reload**: Use `--reload` flag with Uvicorn during development.
- **Testing endpoints**: Use the built-in Swagger UI at `/docs` or tools like Postman/Insomnia.

---

### Troubleshooting

- **Torch / CUDA errors**
  - Make sure your PyTorch installation matches your CUDA version.
  - To force CPU-only execution, configure models accordingly in `app/models/*` or via environment variables.
- **Model download issues**
  - Some models (e.g., CLIP) may be fetched from the internet on first use; ensure the machine has network access.
- **Performance**
  - For production, disable `--reload`, and consider running behind a process manager (e.g., `gunicorn` with `uvicorn.workers.UvicornWorker`) and enabling GPU acceleration.

---

### License

Add your preferred license here (e.g., MIT, Apache 2.0). If this is private/internal, you can simply note that it is **proprietary / internal use only**.

