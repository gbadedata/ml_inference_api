from fastapi.testclient import TestClient
from app.main import app


def test_invalid_payload():
    payload = {
        "features": [5.1, 3.5]
    }

    with TestClient(app) as client:
        response = client.post("/predict", json=payload)

    assert response.status_code == 422