from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator

from app.config import settings
from app.schemas import PredictRequest, PredictResponse
from app.model_loader import load_model
from app.services.predictor import predict
from app.logging_conf import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    app.state.model = load_model(settings.MODEL_PATH)
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)


@app.get("/health/live")
def live():
    return {"status": "alive"}


@app.get("/health/ready")
def ready(request: Request):
    model = getattr(request.app.state, "model", None)
    if model is None:
        return {"status": "not_ready"}
    return {"status": "ready"}


@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request_body: PredictRequest, request: Request):
    model = getattr(request.app.state, "model", None)
    prediction = predict(model, request_body.features)
    return PredictResponse(prediction=prediction)


Instrumentator().instrument(app).expose(app)