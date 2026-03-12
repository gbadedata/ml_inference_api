
# Final Project Report
## ML Inference API — Production‑Style Machine Learning Service

---

# 1. Executive Summary

This project demonstrates how a trained machine learning model can be transformed into a production‑style inference service.

The system moves beyond notebook experimentation and implements the engineering components required to operate ML models as deployable services.

The completed system includes:

• trained machine learning model artifact
• FastAPI inference API
• automated tests using pytest
• Docker containerization
• monitoring with Prometheus and Grafana
• CI/CD pipeline using GitHub Actions
• container publishing to GHCR and Amazon ECR
• Kubernetes deployment configuration
• public deployment on Render
• AWS ECS Fargate deployment behind an Application Load Balancer

The project demonstrates practical ML engineering and deployment practices.

---

# 2. Project Objective

The objective was to build a machine learning inference system that demonstrates how models move from development to deployable infrastructure.

Key goals:

• package an ML model as an API
• implement health checks
• containerize the service
• integrate monitoring
• automate testing and builds
• deploy to cloud infrastructure

---

# 3. System Overview

The system consists of several layers:

ML Layer — model training and artifact serialization  
Application Layer — FastAPI inference API  
Monitoring Layer — Prometheus and Grafana  
Container Layer — Docker runtime  
Delivery Layer — GitHub Actions CI/CD  
Orchestration Layer — Kubernetes manifests  
Cloud Layer — Render and AWS ECS deployment

---

# 4. Machine Learning Component

The model is trained using scikit‑learn and serialized with joblib.

Steps:

1. Train model
2. Serialize artifact
3. Load artifact during API startup
4. Run inference inside FastAPI

This ensures deterministic runtime behaviour and fast inference latency.

---

# 5. API Service

The inference service is implemented using FastAPI.

Endpoints:

GET /health/live  
GET /health/ready  
POST /predict  
GET /metrics  
GET /docs

Swagger UI allows interactive API testing.

---

# 6. Testing

Automated testing is implemented using pytest.

Tests validate:

• API health endpoints
• prediction responses
• error handling
• application startup

---

# 7. Containerization

The service runs inside a Docker container.

Container responsibilities:

• install dependencies
• copy application code
• include trained model artifact
• run the FastAPI server

---

# 8. Monitoring

Prometheus collects metrics from the /metrics endpoint.

Grafana visualizes these metrics.

Monitoring tracks:

• request counts
• request latency
• inference calls
• application health

---

# 9. CI/CD Pipeline

GitHub Actions automates:

GitHub push  
→ run tests  
→ build Docker image  
→ publish image to registries

Images are pushed to:

• GitHub Container Registry
• Amazon Elastic Container Registry

---

# 10. Kubernetes Deployment

Kubernetes configuration includes:

Deployment  
Service  
Horizontal Pod Autoscaler  
Ingress

This supports scalable container deployment.

---

# 11. Render Deployment

The API is publicly deployed using Render.

Verified endpoints:

/docs  
/health/live  
/health/ready  
/predict

---

# 12. AWS ECS Deployment

The application is deployed on AWS ECS Fargate.

Infrastructure:

Amazon ECR  
ECS Cluster  
Task Definition  
ECS Service  
Application Load Balancer  
Target Group  
Security Groups

Traffic flow:

Client → ALB → Target Group → ECS Service → Fargate Task → FastAPI Container

---

# 13. Deployment Verification

ECS service running  
Target group healthy  
ALB endpoints reachable

Example request:

{
 "features": [5.1, 3.5, 1.4, 0.2]
}

Example response:

{
 "prediction": 0
}

---

# 14. Evidence

Screenshots documenting the deployment are stored in:

docs/evidence/

Evidence includes:

• Docker build verification
• GitHub Actions pipeline
• Prometheus metrics
• Grafana dashboards
• Kubernetes pods
• Render deployment
• AWS ECS service running
• ALB endpoint tests

---

# 15. Limitations

This is a demonstration architecture.

Current limitations:

• no authentication
• no rate limiting
• no centralized logging
• no distributed tracing
• no Infrastructure‑as‑Code deployment

---

# 16. Future Improvements

Possible improvements:

• API authentication
• request throttling
• model registry
• centralized logging
• Terraform infrastructure provisioning
• ECS autoscaling policies

---

# 17. Conclusion

This project demonstrates the practical engineering workflow required to run a machine learning inference service in modern cloud environments.
