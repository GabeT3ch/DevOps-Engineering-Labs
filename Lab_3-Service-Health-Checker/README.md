# Lab 3 - Service Health Checker

A Python-based service health monitoring tool that checks the availability and response time of HTTP/HTTPS endpoints. Built as part of a progressive DevOps portfolio demonstrating real operational tooling.

## What It Does

- Reads a list of target services/URLs from a config file
- Sends HTTP requests to each endpoint and checks response codes
- Measures response time for each service
- Classifies each service as UP, DEGRADED, or DOWN
- Logs results to a file and prints a formatted status report
- Alerts when a service is down or response time exceeds a threshold

## Why This Matters

Service health checking is a core DevOps responsibility. Tools like Prometheus, Datadog, and AWS CloudWatch do this at scale — this lab demonstrates understanding of the underlying problem those tools solve.

## Lab Progression

| Lab | Builds On |
|-----|-----------|
| Lab 1 - System Resource Monitor | Baseline scripting and logging |
| Lab 2 - Log Analyzer | Log parsing and report generation |
| **Lab 3 - Service Health Checker** | **HTTP monitoring and alerting** |
| Lab 4 - CI/CD Pipeline | Automates testing and deployment of Labs 1-3 |

## Tools & Technologies

- **Language:** Python 3
- **Libraries:** `requests`, `PyYAML`
- **Config:** YAML
- **OS:** Fedora Linux

## Setup

```bash
pip install -r requirements.txt
python service-health-checker.py
```

## Configuration

Edit `config.yaml` to define which services to monitor, response time thresholds, check intervals, and log file location.

## Example Output

```
Service Health Report - 2026-02-21 15:00:00
==================================================
[UP]       https://example.com          | 120ms
[DEGRADED] https://slow-service.com     | 4500ms
[DOWN]     https://broken-service.com   | TIMEOUT
==================================================
Total: 3 services | UP: 1 | DEGRADED: 1 | DOWN: 1
```