# Architecture Notes — ML Inference API

## Purpose

This document provides a simple architecture reference separate from the README.

It is useful because the README explains the project broadly, while this file isolates the system structure in one place.

---

## 1. Application Architecture

```text
Client
  │
  ▼
FastAPI Inference API
  │
  ▼
Serialized Model Artifact
```

The FastAPI service loads the serialized model artifact during startup and uses it to serve predictions.

---

## 2. Observability Architecture

```text
FastAPI Application
      │
      ▼
/metrics endpoint
      │
      ▼
Prometheus
      │
      ▼
Grafana
```

The application exposes Prometheus-format metrics. Prometheus scrapes those metrics, and Grafana visualizes them.

---

## 3. Delivery Architecture

```text
GitHub Push
   │
   ▼
GitHub Actions
   │
   ├── Run Tests
   ├── Build Docker Image
   └── Push Image to GHCR
```

This supports continuous validation and distribution of the container image.

---

## 4. Kubernetes Architecture

```text
Client
  │
  ▼
Ingress
  │
  ▼
Kubernetes Service
  │
  ▼
FastAPI Pods
  │
  ▼
Model Artifact
```

The Kubernetes deployment adds service routing, autoscaling support, and ingress-based access.

---

## 5. Public Cloud Deployment Architecture

```text
GitHub Repository
   │
   ▼
Render Build
   │
   ▼
Docker Container
   │
   ▼
Public Web Service
```

This gives the project a publicly reachable deployment suitable for demonstration.

---

## 6. Final Interpretation

The project architecture is best understood as a layered ML service system:

- model training and artifact generation
- API serving
- monitoring
- testing
- containerization
- CI/CD
- orchestration
- public deployment

This folder can later be expanded with diagrams if needed, but a simple text architecture reference is already useful and sufficient.
