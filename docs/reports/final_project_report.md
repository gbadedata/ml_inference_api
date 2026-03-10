# Final Project Report — ML Inference API

## Objective

Build a production-style machine learning inference API including monitoring, containerization, CI/CD, Kubernetes deployment, autoscaling, and ingress routing.

## Architecture

Client → Ingress → Kubernetes Service → FastAPI Pods → Model Artifact

Monitoring:

FastAPI /metrics → Prometheus → Grafana

CI/CD:

GitHub → GitHub Actions → Docker Image → GHCR → Kubernetes Pull

## Model

LogisticRegression

Artifact:

model/artifact/model.joblib

## Core Components

Model training  
FastAPI inference API  
Health endpoints  
Prometheus metrics  
pytest tests  
Docker container  
Prometheus monitoring  
Grafana dashboards  
Locust load testing  
GitHub Actions CI/CD  
Kubernetes deployment  
Horizontal Pod Autoscaler  
Ingress routing

## Evidence

Screenshots stored in:

docs/evidence/

## Conclusion

The project demonstrates how a trained machine learning model can be deployed as a scalable inference service using modern cloud-native tooling.