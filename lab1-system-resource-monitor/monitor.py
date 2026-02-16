#!/usr/bin/env python3
"""
System Resource Monitor
Monitors CPU, memory, and disk usage on the local machine.
Logs readings and alerts when thresholds are exceeded.
"""

import psutil
import yaml
import time
import logging
from datetime import datetime


def load_config(config_path="config.yaml"):
    #Load monitoring thresholds and settings from config file.
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config


def setup_logging(log_file):
    #Configure logging to both file and terminal.
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)



def get_system_metrics():
    #Collect current CPU, memory, and disk usage
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_info.percent,
        "disk_percent": (disk_info.used / disk_info.total * 100)
    }


def check_thresholds(metrics, thresholds):
    #Compare current metrics against configured thresholds. Return list of alerts
    alerts = []
    for metric, value in metrics.items():
        if metric in thresholds and value > thresholds[metric]:
            alerts.append(f"Alert: {metric} usage is {value:.2f}%, exceeding threshold of {thresholds[metric]}%")
    return alerts


def main():
    """Main monitoring loop."""
    
    # TODO: Load config
    # TODO: Set up logging
    # TODO: Run a loop that:
    #   1. Gets system metrics
    #   2. Logs the current readings
    #   3. Checks thresholds and logs any alerts
    #   4. Sleeps for the configured interval
    # TODO: Handle KeyboardInterrupt (Ctrl+C) for clean shutdown
    pass


if __name__ == "__main__":
    main()
    config = load_config()
    setup_logging(config['log_file'])
    logging.info("Test message - logging works!")