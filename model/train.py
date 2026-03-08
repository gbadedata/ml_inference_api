from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def main() -> None:
    """
    Train a simple logistic regression model on the Iris dataset
    and save the trained artifact to disk.
    """
    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Train model
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X, y)

    # Ensure artifact directory exists
    artifact_dir = Path("model/artifact")
    artifact_dir.mkdir(parents=True, exist_ok=True)

    # Save trained model
    artifact_path = artifact_dir / "model.joblib"
    joblib.dump(model, artifact_path)

    print(f"Model trained successfully and saved to: {artifact_path}")


if __name__ == "__main__":
    main()