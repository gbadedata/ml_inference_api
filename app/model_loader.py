from pathlib import Path

import joblib


def load_model(model_path: str = "model/artifact/model.joblib"):
    """
    Load the trained model artifact from disk.
    """
    path = Path(model_path)

    if not path.exists():
        raise FileNotFoundError(f"Model artifact not found at: {path}")

    model = joblib.load(path)
    return model


if __name__ == "__main__":
    loaded_model = load_model()
    print("Model loaded successfully.")
    print(f"Loaded model type: {type(loaded_model)}")