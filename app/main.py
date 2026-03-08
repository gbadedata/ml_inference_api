from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.config import settings
from app.schemas import PredictRequest, PredictResponse
from app.model_loader import load_model
from app.services.predictor import predict
from app.logging_conf import setup_logging


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

model = None


@app.on_event("startup")
def startup_event():
    global model
    setup_logging()
    model = load_model(settings.MODEL_PATH)


@app.get("/health/live")
def live():
    return {"status": "alive"}


@app.get("/health/ready")
def ready():
    if model is None:
        return {"status": "not_ready"}
    return {"status": "ready"}


@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest):
    prediction = predict(model, request.features)
    return PredictResponse(prediction=prediction)


Instrumentator().instrument(app).expose(app)