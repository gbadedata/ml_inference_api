# Production-Style ML Inference API with FastAPI, Docker, Prometheus, Grafana, GitHub Actions, Kubernetes, HPA, and Ingress

## Project Summary

This project demonstrates how to build a production-style machine learning inference service from the ground up. It starts with offline model training and artifact serialization, then exposes the model through a FastAPI application with health checks, Prometheus metrics, automated tests, containerization, CI/CD, Kubernetes deployment, horizontal pod autoscaling, and ingress-based routing.

The goal of this project is not just to train a model, but to show the engineering practices required to operate a machine learning model as a service.

## What This Project Includes

- offline model training and artifact saving
- FastAPI inference API
- request and response validation with Pydantic
- liveness and readiness endpoints
- Prometheus metrics exposure
- automated testing with pytest
- Docker containerization
- Docker Compose observability stack with Prometheus and Grafana
- load testing with Locust
- GitHub Actions CI/CD
- Docker image publishing to GitHub Container Registry (GHCR)
- Kubernetes deployment and service routing
- resource requests and limits
- Horizontal Pod Autoscaler (HPA)
- ingress-based access using ingress-nginx

## Tech Stack

- Python
- FastAPI
- scikit-learn
- NumPy
- joblib
- pytest
- Docker
- Docker Compose
- Prometheus
- Grafana
- Locust
- GitHub Actions
- GitHub Container Registry (GHCR)
- Kubernetes
- ingress-nginx

## Architecture

### Local and container architecture

Client  
→ FastAPI API  
→ Model artifact  
→ `/metrics`  
→ Prometheus  
→ Grafana  

### Kubernetes architecture

Client  
→ Ingress  
→ Kubernetes Service  
→ FastAPI Pods  
→ Model artifact  

### Delivery architecture

GitHub Push  
→ GitHub Actions  
→ Run Tests  
→ Build Docker Image  
→ Push to GHCR  
→ Kubernetes pulls image  

## API Endpoints

### `GET /health/live`
Returns application liveness status.

Example response:

```json
{"status":"alive"}


GET /health/ready

Returns readiness status after model loading.

Example response:

{"status":"ready"}
POST /predict

Runs inference using the trained model.

Example request:

{
  "features": [5.1, 3.5, 1.4, 0.2]
}

Example response:

{
  "prediction": 0
}

GET /health/live  
GET /health/ready  
POST /predict  
GET /metrics  
GET /docs

## Project Structure

ml_inference_api/
├── .github/
├── app/
├── model/
├── tests/
├── monitoring/
├── k8s/
├── load_tests/
├── scripts/
├── docs/
│ ├── evidence/
│ ├── reports/
│ └── architecture/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── README.md

## Evidence

Project verification screenshots are stored in:

docs/evidence/

Evidence mapping:

docs/evidence/evidence_index.md

## Cloud Deployment

The containerized ML inference API was deployed to Render as a public web service using the project’s GitHub repository and Dockerfile.

Cloud deployment verified:
- public URL reachable
- `/docs` available
- `/health/live` available
- `/health/ready` available
- `/predict` returning successful inference

Note: the Render deployment uses a free web service instance for demonstration purposes.