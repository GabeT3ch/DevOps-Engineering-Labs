# Lab 01 - System Resource Monitor

## Overview

A Python script that monitors local system resources (CPU, memory, disk) and logs alerts when usage exceeds configurable thresholds. Built and tested on Fedora Linux.

This is the kind of quick automation a DevOps engineer writes to eliminate manual server checks — run it on a box, let it watch the resources, and log warnings before things go sideways.

## What This Lab Covers

- Python scripting for systems automation
- Working with the `psutil` library for system metrics
- Logging with timestamps
- Configurable thresholds via a simple config
- Error handling for production-quality scripts

## Environment

- **OS:** Fedora Linux (tested on main workstation)
- **Python:** 3.x
- **Future labs** will deploy this script to remote infrastructure (VMs) using Ansible and containerize it with Docker

## Setup

```bash
# Install dependency
pip install psutil

# Run the monitor
python3 monitor.py
```

## Configuration

Edit the thresholds in `config.yaml` to set your own alert levels:

```yaml
thresholds:
  cpu_percent: 80
  memory_percent: 85
  disk_percent: 90

interval_seconds: 10
log_file: "monitor.log"
```

## What It Does

1. Checks CPU usage, memory usage, and disk usage at a set interval
2. Logs all readings with timestamps to a log file
3. Prints a warning to the terminal and log when any threshold is exceeded
4. Runs continuously until stopped with `Ctrl+C`

## Example Output

```
[2026-02-12 19:30:01] CPU: 23% | Memory: 61% | Disk: 45%
[2026-02-12 19:30:11] CPU: 87% | Memory: 61% | Disk: 45%
[2026-02-12 19:30:11] ⚠ ALERT: CPU usage at 87% (threshold: 80%)
```

## File Structure

```
lab-01-system-resource-monitor/
├── README.md
├── config.yaml
├── monitor.py
└── monitor.log (generated at runtime)
```

## Skills Demonstrated

- Python systems scripting
- Linux resource monitoring fundamentals
- Logging and alerting patterns
- Clean code structure with error handling
- YAML configuration management