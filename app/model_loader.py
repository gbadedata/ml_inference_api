from pathlib import Path
import joblib


def load_model(model_path: str):
    """
    Load trained model artifact.
    """
    path = Path(model_path)

    if not path.exists():
        raise FileNotFoundError(f"Model artifact not found at {path}")

    model = joblib.load(path)
    return model