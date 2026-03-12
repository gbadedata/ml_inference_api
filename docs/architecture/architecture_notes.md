
# Architecture Notes — ML Inference API

## Purpose

This document describes the system architecture used to run the **ML Inference API** as a production‑style machine learning service.  
The architecture demonstrates how a trained ML model is packaged, exposed through an API, monitored, containerized, and deployed to cloud infrastructure.

The focus is **engineering architecture**, not model research.

---

# 1. Core Application Architecture

The core service is a FastAPI application that loads a trained model artifact and exposes prediction endpoints.

Flow:

Client  
→ FastAPI API  
→ Model Artifact  
→ Prediction Response

Details:

• The ML model is trained offline using **scikit‑learn**.  
• The trained model is serialized using **joblib**.  
• The artifact is loaded at API startup.  
• Inference is executed inside the FastAPI service.  

Key properties:

• low‑latency inference  
• stateless API container  
• container‑friendly runtime

---

# 2. API Layer

The API layer is implemented using **FastAPI**.

Responsibilities:

• request validation using Pydantic  
• prediction execution  
• health checks for infrastructure monitoring  
• metrics exposure for Prometheus

Endpoints:

GET /health/live  
GET /health/ready  
POST /predict  
GET /metrics  
GET /docs

The `/docs` endpoint exposes the **Swagger UI** for interactive testing.

---

# 3. Monitoring Architecture

Monitoring is implemented using **Prometheus and Grafana**.

Flow:

FastAPI Application  
→ /metrics endpoint  
→ Prometheus Scraper  
→ Grafana Dashboard

Responsibilities:

Prometheus

• scrape metrics from the application  
• store time‑series metrics

Grafana

• visualize metrics
• create monitoring dashboards

Metrics collected include:

• request count
• request latency
• application health
• inference calls

---

# 4. Container Architecture

The service runs inside a **Docker container**.

Container responsibilities:

• install dependencies  
• copy application code  
• include trained model artifact  
• start FastAPI server with Uvicorn

Startup command:

Uvicorn runs the FastAPI app and exposes port **8000**.

Container advantages:

• reproducible environment  
• portable deployment  
• consistent runtime across systems

---

# 5. CI/CD Architecture

Continuous integration is implemented using **GitHub Actions**.

Flow:

GitHub Push  
→ GitHub Actions Pipeline  
→ Run Tests  
→ Build Docker Image  
→ Push Image to Container Registry

Container registries used:

• GitHub Container Registry (GHCR)  
• Amazon Elastic Container Registry (ECR)

Pipeline responsibilities:

• run automated tests  
• validate build  
• publish container image

---

# 6. Kubernetes Architecture

The application can run inside **Kubernetes**.

Flow:

Client  
→ Ingress Controller  
→ Kubernetes Service  
→ FastAPI Pods

Components:

Deployment

• manages FastAPI pods

Service

• exposes pods internally

Horizontal Pod Autoscaler (HPA)

• scales pods based on CPU usage

Ingress

• routes external traffic to the service

Benefits:

• scalability
• container orchestration
• rolling deployments

---

# 7. AWS Deployment Architecture

The system is deployed to **AWS ECS Fargate**.

Infrastructure components:

Amazon ECR  
ECS Cluster  
Task Definition  
ECS Service  
Application Load Balancer  
Target Group  
Security Groups

Traffic flow:

Client  
→ Application Load Balancer (ALB)  
→ Target Group  
→ ECS Service  
→ Fargate Task  
→ FastAPI Container  
→ Model Artifact

---

# 8. Network Security Model

Two security groups control traffic.

ALB Security Group

Inbound:

HTTP 80 from internet

Outbound:

All traffic allowed

Task Security Group

Inbound:

TCP 8000 from ALB security group only

Outbound:

All traffic allowed

This prevents direct public access to the container tasks.

---

# 9. Health Check Architecture

The load balancer monitors container health.

Target Group health check:

Protocol: HTTP  
Port: 8000  
Path: /health/live  
Success code: 200

If the container fails health checks:

• the task is considered unhealthy  
• ECS replaces the task automatically

---

# 10. Request Flow in Production

Complete request path:

User Request  
→ Internet  
→ Application Load Balancer  
→ Target Group  
→ ECS Service  
→ Fargate Task  
→ FastAPI Container  
→ ML Model  
→ Prediction Response

---

# 11. System Characteristics

The architecture demonstrates:

• stateless API containers  
• containerized ML inference  
• infrastructure health monitoring  
• container registry deployment  
• load balanced cloud services

This structure mirrors the architecture used by many real production ML systems.

---

# 12. Known Limitations

This architecture is intentionally simplified for demonstration purposes.

Limitations:

• no authentication layer  
• no rate limiting  
• no model registry  
• no distributed tracing  
• no centralized logging stack  
• no Infrastructure‑as‑Code provisioning

---

# 13. Possible Improvements

Future engineering improvements could include:

• Terraform infrastructure provisioning  
• API authentication  
• request throttling  
• centralized logging (ELK or OpenSearch)  
• distributed tracing (OpenTelemetry)  
• model version registry  
• ECS autoscaling policies
