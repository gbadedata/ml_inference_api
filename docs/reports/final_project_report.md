# Final Project Report — ML Inference API

## 1. Executive Summary

This project demonstrates how to turn a trained machine learning model into a production-style inference service.

The system trains a model offline, serializes the artifact, exposes it through a FastAPI application, validates requests, emits Prometheus metrics, supports automated testing, runs inside Docker, integrates with GitHub Actions and GitHub Container Registry (GHCR), deploys to Kubernetes with autoscaling and ingress, and is also publicly deployed as a managed cloud web service.

The purpose of the project is not only to build a model, but to show the engineering workflow required to operate machine learning systems outside notebooks.

---

## 2. Project Objective

The objective of the project was to build a production-style ML inference API that includes:

- offline model training
- reusable model artifact loading
- FastAPI-based inference serving
- health and readiness checks
- Prometheus metrics
- automated testing
- Docker containerization
- observability with Prometheus and Grafana
- load testing with Locust
- CI/CD with GitHub Actions
- container publishing to GHCR
- Kubernetes deployment
- Horizontal Pod Autoscaler (HPA)
- ingress-based routing
- public cloud deployment

This project was designed to bridge the gap between model development and deployment-oriented ML engineering.

---

## 3. Final System Scope

The final system includes the following verified capabilities:

### Machine Learning
- model training with scikit-learn
- artifact serialization using `joblib`
- repeatable artifact creation during Docker image build

### API Service
- FastAPI inference service
- request validation with Pydantic
- structured prediction response
- liveness endpoint
- readiness endpoint
- Swagger UI

### Testing
- pytest coverage for health, prediction, invalid payloads, and metrics

### Observability
- Prometheus metrics endpoint
- Prometheus scraping validation
- Grafana dashboard validation
- load testing with Locust

### Containerization and Delivery
- Docker build
- Docker runtime verification
- Docker Compose observability stack
- GitHub Actions workflow
- image publishing to GHCR
- image pull verification

### Orchestration
- Kubernetes namespace
- deployment
- service
- Prometheus manifests
- resource requests and limits
- rolling update strategy
- HPA
- ingress controller
- ingress resource and hostname routing

### Public Deployment
- Docker-based managed deployment on Render
- public `/docs`, `/health/live`, `/health/ready`, and `/predict`

---

## 4. Verified Model and Artifact

The final verified model used in this project is:

- **Model type:** `LogisticRegression`
- **Artifact path:** `model/artifact/model.joblib`

The training script is stored in:

`model/train.py`

The model loader is stored in:

`app/model_loader.py`

A key improvement made during the project was moving artifact generation into the Docker build process so that deployments do not depend on a locally pre-existing model file.

---

## 5. Repository Structure

The repository is organized to separate application code, infrastructure, monitoring, tests, and project documentation.

```text
ml_inference_api/
├── .github/
│   └── workflows/
├── app/
├── model/
│   └── artifact/
├── tests/
├── monitoring/
├── k8s/
├── load_tests/
├── scripts/
├── docs/
│   ├── evidence/
│   ├── reports/
│   └── architecture/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── README.md
```

This structure supports maintainability and makes the project easier to review and reproduce.

---

## 6. Architecture

### Application Flow

Client  
→ FastAPI Inference API  
→ Model Artifact  

### Observability Flow

FastAPI `/metrics`  
→ Prometheus  
→ Grafana  

### Delivery Flow

GitHub Push  
→ GitHub Actions  
→ Run Tests  
→ Build Docker Image  
→ Push to GHCR  

### Kubernetes Flow

Client  
→ Ingress  
→ Kubernetes Service  
→ FastAPI Pods  
→ Model Artifact  

### Public Cloud Flow

GitHub Repository  
→ Render Build  
→ Docker Container  
→ Public Web Service  

---

## 7. API Surface

The application exposes the following endpoints:

### `GET /health/live`
Returns:

```json
{"status":"alive"}
```

### `GET /health/ready`
Returns:

```json
{"status":"ready"}
```

### `POST /predict`
Accepts a request body such as:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Returns a prediction such as:

```json
{
  "prediction": 0
}
```

### `GET /metrics`
Exposes Prometheus-formatted metrics.

### `GET /docs`
Provides Swagger UI for interactive testing.

---

## 8. Development Progression

The project evolved through the following engineering stages:

1. repository structure and virtual environment setup
2. model training and artifact creation
3. FastAPI API implementation
4. Prometheus instrumentation
5. pytest automation
6. Docker containerization
7. Docker Compose observability stack
8. load testing with Locust
9. GitHub Actions CI pipeline
10. GHCR image publishing
11. Kubernetes deployment
12. HPA and resource controls
13. ingress routing
14. public cloud deployment on Render

This progression is important because it shows that the project was built incrementally rather than assembled as disconnected pieces.

---

## 9. Major Errors Encountered and How They Were Fixed

Several important failures occurred during the project. These failures were not wasted effort; they improved the final system design.

### 9.1 Python packaging and pytest import failures
Problem:
`ModuleNotFoundError: No module named 'app'`

Fix:
- added `__init__.py` files
- added `pytest.ini`
- stabilized import resolution

### 9.2 Startup model loading weakness
Problem:
readiness and prediction tests failed because the model was not reliably initialized

Fix:
- replaced fragile startup approach with FastAPI lifespan handling
- stored the model in `app.state.model`

### 9.3 Deprecated startup event usage
Problem:
deprecated `@app.on_event("startup")` pattern

Fix:
- migrated to lifespan-based startup

### 9.4 CI artifact absence
Problem:
CI tests failed because the model artifact was not available in the remote runner

Fix:
- added model training to the CI workflow

### 9.5 Missing dependency for test client
Problem:
`httpx` missing during CI execution

Fix:
- added `httpx` to requirements

### 9.6 GHCR push authentication failure
Problem:
Docker push to GHCR failed due to missing authentication

Fix:
- authenticated Docker using GitHub PAT
- verified image push and pull

### 9.7 Kubernetes YAML encoding issue
Problem:
`no objects passed to apply`

Fix:
- rewrote manifests in UTF-8 encoding

### 9.8 Metrics server failure on Docker Desktop
Problem:
metrics-server failed due to kubelet TLS validation

Fix:
- adjusted metrics-server deployment to tolerate insecure kubelet TLS in local cluster context

### 9.9 Cloud deployment artifact failure
Problem:
Render deployment failed because `model/artifact/model.joblib` was not present in the remote build output

Fix:
- changed Dockerfile to run `python model/train.py` during image build
- made the image self-contained and reproducible

These fixes materially improved the reliability of the final system.

---

## 10. Deployment Environments Verified

### Local Runtime
Validated:
- app startup
- Swagger access
- health endpoints
- prediction endpoint
- metrics endpoint

### Docker Runtime
Validated:
- image build
- container startup
- endpoint access inside container

### Docker Compose Stack
Validated:
- Prometheus target scraping
- Grafana dashboard availability

### CI/CD
Validated:
- workflow success
- test job success
- build-and-push success
- image availability in GHCR

### Kubernetes
Validated:
- pods running
- service created
- health and prediction access
- HPA metrics
- resource limits
- rolling strategy
- ingress routing

### Public Cloud
Validated:
- Render deployment success
- public Swagger
- public health endpoints
- public prediction access

---

## 11. Evidence

Project screenshots and verification files are stored in:

`docs/evidence/`

The evidence index is stored in:

`docs/evidence/evidence_index.md`

The evidence set covers the entire project progression, including local testing, Docker, observability, CI/CD, Kubernetes, ingress, and public deployment.

---

## 12. Current Strengths

This project demonstrates real engineering strengths in the following areas:

- machine learning artifact management
- API design and validation
- automated testing
- containerization
- observability exposure
- CI/CD workflow execution
- image registry publishing
- Kubernetes deployment
- autoscaling concepts
- ingress routing
- public cloud deployment

That is strong portfolio material for deployment-oriented AI and ML engineering roles.

---

## 13. Limitations

This project is **production-style**, not a hardened enterprise deployment.

Current limitations include:

- no authentication or API key protection
- no rate limiting
- no formal model registry
- no secret management workflow
- no distributed tracing
- no alerting rules configured
- no centralized log aggregation
- no managed cloud Kubernetes deployment
- no blue/green or canary release strategy
- free-tier Render cold starts after inactivity

These limits do not invalidate the project, but they define its real scope.

---

## 14. Future Improvements

Natural next improvements would include:

- API authentication and authorization
- rate limiting
- structured inference logging
- model versioning and registry integration
- alerting through Prometheus and Grafana
- infrastructure-as-code provisioning
- deployment to managed cloud Kubernetes
- progressive delivery strategies
- stronger operational security controls

---

## 15. Final Assessment

This project is no longer a notebook-level ML exercise.

It is an end-to-end, production-style ML inference service that demonstrates how to:

- train and package a model
- serve predictions through an API
- instrument the service for monitoring
- test the service automatically
- containerize and publish the application
- deploy it through Kubernetes and cloud platforms
- expose it publicly for use

The project should be presented honestly as a **production-style ML inference system with strong engineering coverage**, not as a fully hardened enterprise platform.
