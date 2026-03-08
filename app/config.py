from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ML Inference API"
    APP_VERSION: str = "1.0.0"
    MODEL_PATH: str = "model/artifact/model.joblib"
    LOG_LEVEL: str = "INFO"


settings = Settings()