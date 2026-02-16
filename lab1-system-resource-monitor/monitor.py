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
    """Load monitoring thresholds and settings from config file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config


def setup_logging(log_file):
    """Configure logging to both file and terminal."""
    # TODO: Set up logging so output goes to both the log file AND the terminal
    # HINT: Look into logging.basicConfig() and logging.StreamHandler()
    pass


def get_system_metrics():
    """Collect current CPU, memory, and disk usage."""
    # TODO: Use psutil to grab CPU percent, memory percent, and disk percent
    # TODO: Return them in a dictionary
    # HINT: psutil.cpu_percent(), psutil.virtual_memory(), psutil.disk_usage('/')
    pass


def check_thresholds(metrics, thresholds):
    """Compare current metrics against configured thresholds. Return list of alerts."""
    # TODO: Loop through the metrics and compare each one to its threshold
    # TODO: Return a list of alert messages for anything that exceeds its threshold
    pass


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
    print(load_config("config.yml"))