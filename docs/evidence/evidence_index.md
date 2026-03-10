# Evidence Index — ML Inference API

## Core API and model
01_train_script.png — model training script
02_training_success.png — successful model training run
03_model_artifact_exists.png — trained model artifact saved
04_sample_input_file.png — sample inference payload file
05_model_loader_success.png — model artifact successfully loaded
06_fastapi_startup.png — FastAPI application startup
07_health_endpoint.png — liveness endpoint working
08_ready_endpoint.png — readiness endpoint working
09_swagger_docs.png — Swagger UI available
10_prediction_test.png — prediction endpoint successful
11_metrics_endpoint.png — Prometheus metrics endpoint exposed
12_pytest_success.png — automated tests passed
13_fastapi_lifespan_recheck.png — lifespan startup validation

## Docker
14_docker_build_success.png — Docker image built successfully
15_docker_container_running.png — container started successfully
16_container_prediction_test.png — prediction endpoint working inside container
17_container_metrics_endpoint.png — metrics endpoint working inside container

## Docker Compose observability
18_docker_compose_stack_running.png — Docker Compose stack running
19_prometheus_targets_up.png — Prometheus target scraping API successfully
20_grafana_dashboard.png — Grafana dashboard showing live metrics

## Load testing
21_locust_dashboard.png — Locust dashboard showing active load test
22_locust_request_stats.png — request statistics from Locust
23_prometheus_load_metrics.png — Prometheus reflecting load traffic
24_grafana_load_spike.png — Grafana visualizing traffic spike under load

## CI/CD and registry publishing
25_github_actions_workflow_success.png — GitHub Actions workflow completed successfully
26_test_job_success.png — CI test stage passed
27_build_push_job_success.png — Docker build and push stage passed
28_ghcr_package_visible.png — GHCR package visible in GitHub Packages
29_docker_pull_ghcr_success.png — image pulled successfully from GHCR

## Kubernetes deployment
30_k8s_swagger_ui.png — Swagger UI accessible from Kubernetes deployment
31_k8s_metrics_endpoint.png — metrics endpoint accessible in Kubernetes
32_k8s_pods_running.png — Kubernetes pods running
33_k8s_service_list.png — Kubernetes service created
34_k8s_health_live.png — liveness endpoint working in Kubernetes
35_k8s_prediction_request.png — prediction endpoint working in Kubernetes

## Production hardening
36_metrics_server_running.png — metrics-server installed and running
37_hpa_working.png — Horizontal Pod Autoscaler working
38_deployment_resource_limits.png — deployment resource requests and limits configured
39_rolling_update_strategy.png — rolling update strategy verified

## Ingress
40_ingress_controller_running.png — ingress controller running
41_ingressclass_present.png — ingress class available
42_ingress_resource_created.png — ingress resource created
43_ingress_docs_via_hostname.png — Swagger UI reachable through ingress hostname
44_ingress_health_live.png — health endpoint reachable through ingress
45_ingress_predict_success.png — prediction endpoint reachable through ingress