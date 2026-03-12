
# ML Inference API

Production‑style machine learning inference service demonstrating how to take a trained ML model and deploy it as a scalable API with monitoring, containerization, CI/CD, Kubernetes, and cloud infrastructure.

---

# Project Overview

This project demonstrates the **full engineering lifecycle of a machine learning service**, moving beyond notebook experiments into a real deployable system.

The system performs the following:

• Train a machine learning model offline  
• Serialize the trained model artifact  
• Serve predictions through a **FastAPI inference API**  
• Validate requests and responses with **Pydantic**  
• Provide **health endpoints** for infrastructure monitoring  
• Expose **Prometheus metrics**  
• Run **automated tests using pytest**  
• Package the service with **Docker**  
• Monitor the system with **Prometheus and Grafana**  
• Perform **load testing using Locust**  
• Build and publish images via **GitHub Actions CI/CD**  
• Deploy container images to **GitHub Container Registry and Amazon ECR**  
• Deploy to **Kubernetes with HPA and ingress**  
• Deploy publicly using **Render**  
• Deploy using **AWS ECS Fargate behind an Application Load Balancer**

This project focuses on **ML engineering and deployment practices**, not just model training.

---

# Live Deployments

## Render Deployment

Public service:

https://ml-inference-api-tagq.onrender.com

Swagger UI:

https://ml-inference-api-tagq.onrender.com/docs

---

## AWS ECS Fargate Deployment

The application is deployed using:

• Amazon ECS Fargate  
• Application Load Balancer  
• Target Groups with health checks  
• Security groups controlling network access  

Endpoints exposed through ALB:

GET /health/live  
GET /health/ready  
GET /docs  
POST /predict

---

# Technology Stack

## Programming
Python

## Machine Learning
scikit‑learn  
NumPy  
joblib

## API Layer
FastAPI  
Pydantic  
Uvicorn

## Testing
pytest

## Containerization
Docker  
Docker Compose

## Observability
Prometheus  
Grafana

## Load Testing
Locust

## CI/CD
GitHub Actions

## Container Registries
GitHub Container Registry (GHCR)  
Amazon Elastic Container Registry (ECR)

## Orchestration
Kubernetes  
Ingress NGINX

## Cloud Platforms
Render  
AWS ECS Fargate  
AWS Application Load Balancer

---

# System Architecture

## Local Development Flow

Client  
→ FastAPI API  
→ Model Artifact  
→ Metrics Endpoint  
→ Prometheus  
→ Grafana

---

## CI/CD Flow

GitHub Push  
→ GitHub Actions  
→ Run Tests  
→ Build Docker Image  
→ Push Image to GHCR / ECR

---

## Kubernetes Deployment Flow

Client  
→ Ingress Controller  
→ Kubernetes Service  
→ FastAPI Pods  
→ Model Artifact

---

## AWS Deployment Flow

Client  
→ Application Load Balancer  
→ Target Group  
→ ECS Service  
→ Fargate Task  
→ FastAPI Container  
→ Model Artifact

---

# API Endpoints

## Health Check

### GET /health/live

Returns application liveness status.

Example response:

{
 "status": "alive"
}

---

### GET /health/ready

Returns readiness status once the model has loaded successfully.

Example response:

{
 "status": "ready"
}

---

## Prediction

### POST /predict

Runs inference using the trained model.

Example request:

{
 "features": [5.1, 3.5, 1.4, 0.2]
}

Example response:

{
 "prediction": 0
}

---

## Monitoring

GET /metrics

Prometheus metrics endpoint.

---

## Documentation

GET /docs

Interactive Swagger UI for testing endpoints.

---

# Project Structure

ml_inference_api/

app/  
model/  
tests/  
monitoring/  
k8s/  
load_tests/  
scripts/  

docs/  
docs/evidence/  
docs/reports/  
docs/architecture/  

Dockerfile  
docker-compose.yml  
requirements.txt  
README.md  

---

# Evidence

Verification screenshots are stored in:

docs/evidence/

Evidence includes:

• local API testing  
• Docker build and runtime verification  
• Prometheus scraping targets  
• Grafana dashboards  
• Locust load testing  
• GitHub Actions CI success  
• GHCR container publishing  
• Kubernetes deployments and pods  
• Horizontal Pod Autoscaler behaviour  
• ingress routing  
• Render public deployment  
• AWS ECS deployment  
• AWS target group healthy status  
• ALB endpoint verification

---

# Deployment Summary

## Local

FastAPI application startup verified  
Swagger UI accessible  
Prediction endpoint tested

## Docker

Image built successfully  
Container runtime validated

## Docker Compose Monitoring

Prometheus scraping confirmed  
Grafana dashboards operational

## CI/CD

GitHub Actions pipeline successful  
Docker image pushed to GHCR

## Kubernetes

Deployment applied successfully  
Pods healthy  
HPA configured  
Ingress routing functional

## Render

Deployment successful  
Public endpoints verified

## AWS ECS Fargate

ECR repository created  
Docker image pushed to ECR  
ECS cluster created  
Task definition created  
ECS service deployed  
Application Load Balancer configured  
Target group healthy  
Public endpoints verified

---

# Limitations

This project demonstrates **production‑style engineering practices** but is not a hardened enterprise deployment.

Current limitations:

• No authentication layer  
• No rate limiting  
• No model registry  
• No centralized logging stack  
• No distributed tracing  
• No Infrastructure‑as‑Code deployment  
• ECS service uses a single task instead of autoscaling policies

---

# Future Improvements

Possible improvements:

• API authentication  
• request throttling  
• model versioning and registry integration  
• centralized logging  
• infrastructure‑as‑code using Terraform  
• ECS autoscaling policies  
• advanced monitoring and alerting

---

# What This Project Demonstrates

This project demonstrates practical ML engineering capability in:

• ML artifact management  
• API design and validation  
• automated testing  
• observability integration  
• containerization  
• CI/CD workflows  
• Kubernetes orchestration  
• cloud deployment  
• AWS container deployment and load balancing
