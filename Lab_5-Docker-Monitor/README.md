# Lab 05 - Dockerize System Resource Monitor

## Overview

Containerize Lab 1's System Resource Monitor using Docker. The script that monitors CPU, memory, and disk usage is packaged into a Docker image that can run on any machine with Docker installed — no need to manually install Python or dependencies.

This is a core DevOps skill. In production environments, applications are containerized so they run consistently across development, staging, and production — eliminating "it works on my machine" problems.

## What This Lab Covers

- Writing a Dockerfile from scratch
- Building Docker images with `docker build`
- Running containers with `docker run`
- Understanding Docker layers and image optimization
- Passing configuration into containers with volume mounts
- Viewing container logs with `docker logs`

## Prerequisites

- Docker installed on Fedora (`sudo dnf install docker`)
- Lab 1 System Resource Monitor completed

## File Structure

```
Lab_5-Docker-Monitor/
├── README.md
├── Dockerfile
├── monitor.py          (copied from Lab 1)
├── config.yaml         (copied from Lab 1)
└── requirements.txt
```

## Setup

```bash
# Build the Docker image
docker build -t system-monitor .

# Run the container
docker run system-monitor

# Run in background (detached mode)
docker run -d --name monitor system-monitor

# View logs from running container
docker logs monitor

# Stop the container
docker stop monitor

# Remove the container
docker rm monitor
```

## How It Works

1. The Dockerfile starts with a base Python image
2. Copies the monitor script, config, and requirements into the container
3. Installs dependencies (psutil, pyyaml)
4. Sets the default command to run the monitor script
5. When you run `docker run`, the container starts monitoring system resources just like running the script locally

## Key Concepts

- **Dockerfile** — a recipe that tells Docker how to build your image
- **Image** — a snapshot of your application and its dependencies, built from the Dockerfile
- **Container** — a running instance of an image
- **Layers** — each line in the Dockerfile creates a layer, cached for faster rebuilds

## Skills Demonstrated

- Docker containerization
- Dockerfile best practices
- Container lifecycle management (build, run, stop, remove)
- Packaging Python applications for deployment
- Foundation for Kubernetes and CI/CD container workflows