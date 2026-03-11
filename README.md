# ML Inference API --- Production-Style ML Inference Service

## Overview

This project demonstrates how to take a trained machine learning model
beyond notebook experimentation and operate it as a service.

The system trains a model offline, serializes the artifact, exposes it
through a FastAPI inference API, validates requests, emits Prometheus
metrics, runs automated tests, packages the application with Docker,
supports observability with Prometheus and Grafana, performs load
testing with Locust, publishes container images to GitHub Container
Registry (GHCR), and deploys the service through Kubernetes, ingress,
and a public cloud web service.

This is a production-style project focused on engineering practice
rather than only model training.

------------------------------------------------------------------------

## Live Deployment

Public service https://ml-inference-api-tagq.onrender.com

Swagger interface https://ml-inference-api-tagq.onrender.com/docs

Health endpoints GET /health/live GET /health/ready

Metrics GET /metrics

Prediction endpoint POST /predict

------------------------------------------------------------------------

## Project Objective

Most ML tutorials stop after training a model. Real systems require
additional engineering layers including: - repeatable model packaging -
API design and validation - automated testing - observability -
containerization - deployment workflows - infrastructure exposure

This project demonstrates the path from: Trained model → API service →
container → monitored deployment

------------------------------------------------------------------------

## Core Features

Machine Learning - offline model training with scikit-learn - serialized
model artifact using joblib - reproducible artifact generation during
Docker build

API - FastAPI inference service - request and response validation with
Pydantic - health endpoints for liveness and readiness - automatic
Swagger documentation

Testing - automated API tests using pytest - validation of prediction,
health checks, and invalid payloads

Observability - Prometheus metrics exposure - Prometheus target
validation - Grafana dashboard visualization - load testing with Locust

Containerization - Docker image build - container runtime validation -
Docker Compose observability stack

Delivery and Registry - GitHub Actions CI pipeline - Docker image
publishing to GHCR - remote container pull verification

Orchestration - Kubernetes deployment and service - resource requests
and limits - rolling deployment strategy - Horizontal Pod Autoscaler
(HPA) - ingress-nginx controller and ingress routing

Cloud Deployment - public Docker deployment on Render - successful
application startup in managed environment - public API access

------------------------------------------------------------------------

## Technology Stack

Programming and ML - Python - scikit-learn - NumPy - joblib

API - FastAPI - Pydantic - Uvicorn

Testing - pytest

Containerization - Docker - Docker Compose

Observability - Prometheus - Grafana - Locust -
prometheus-fastapi-instrumentator

CI/CD and Registry - GitHub Actions - GitHub Container Registry (GHCR)

Infrastructure - Kubernetes - ingress-nginx - Render

------------------------------------------------------------------------

## Architecture

Local and container flow Client → FastAPI API → Model Artifact → Metrics
→ Prometheus → Grafana

Delivery pipeline GitHub Push → GitHub Actions → Run Tests → Build
Docker Image → Push to GHCR → Deployment platform pulls image

Kubernetes flow Client → Ingress → Kubernetes Service → FastAPI Pods →
Model Artifact

Public deployment flow GitHub Repository → Docker Build → Model Artifact
Generated → Public Web Service

------------------------------------------------------------------------

## API Endpoints

GET /health/live\
Returns liveness status.

Example { "status": "alive" }

GET /health/ready\
Returns readiness status after model loads.

Example { "status": "ready" }

POST /predict\
Runs inference using the trained model.

Example request { "features": \[5.1, 3.5, 1.4, 0.2\] }

Example response { "prediction": 0 }

GET /metrics\
Prometheus metrics endpoint.

GET /docs\
Swagger UI interface.

------------------------------------------------------------------------

## Project Structure

ml_inference_api/

.github/\
app/\
model/\
tests/\
monitoring/\
k8s/\
load_tests/\
scripts/\
docs/

Dockerfile\
docker-compose.yml\
requirements.txt\
requirements-dev.txt\
pytest.ini\
README.md

------------------------------------------------------------------------

## Evidence

Verification screenshots are stored in

docs/evidence/

Evidence index

docs/evidence/evidence_index.md

Evidence includes

-   local API validation
-   Docker build and container runtime
-   Prometheus scraping targets
-   Grafana dashboard
-   Locust load testing
-   GitHub Actions CI success
-   GHCR container publishing
-   Kubernetes deployment and pods
-   Horizontal Pod Autoscaler behaviour
-   ingress routing
-   public Render deployment

------------------------------------------------------------------------

## Deployment Summary

This project has been verified across multiple environments.

Local - FastAPI application start verified - Swagger and prediction
tested

Docker - image built successfully - container runtime verified

Docker Compose Observability Stack - Prometheus scraping confirmed -
Grafana dashboard operational

CI/CD - GitHub Actions pipeline passed - Docker image pushed to GHCR

Kubernetes - deployment applied successfully - pods healthy - HPA
configured - ingress routing functional

Cloud Deployment - Render deployment successful - model artifact
generated during build - public endpoints verified

------------------------------------------------------------------------

## Limitations

This project demonstrates production-style engineering patterns but is
not a hardened enterprise deployment.

Limitations include

-   no authentication or API key protection
-   no rate limiting
-   no formal model registry
-   no secrets management workflow
-   no distributed tracing
-   no alerting rules configured
-   no centralized log aggregation
-   no managed Kubernetes cluster
-   no canary or blue/green release strategy
-   Render free-tier cold start behaviour

------------------------------------------------------------------------

## Future Improvements

Possible improvements

-   API authentication
-   request throttling
-   model versioning and registry integration
-   structured prediction logging
-   alerting with Prometheus and Grafana
-   infrastructure-as-code provisioning
-   managed Kubernetes deployment
-   progressive deployment strategies

------------------------------------------------------------------------

## What This Project Demonstrates

This project demonstrates applied engineering capability in

-   ML artifact management
-   inference API design
-   automated testing
-   observability integration
-   containerization
-   CI/CD workflows
-   container registry publishing
-   Kubernetes orchestration
-   autoscaling
-   ingress routing
-   public cloud deployment

It represents an end-to-end machine learning inference service rather
than a notebook-only model experiment.
