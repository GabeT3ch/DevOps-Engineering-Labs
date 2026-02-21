# Service Health Checker - Monitors HTTP/HTTPS endpoints and reports availability and response time.

import requests
import yaml
import logging
import time
from datetime import datetime


def load_config(config_path="config.yaml"):
    # Load list of services to monitor and settings from config file.
    # Use yaml.safe_load just like Lab 1 and return the config dict.
    pass


def setup_logging(log_file):
    # Configure logging to both file and terminal.
    # Same pattern as Lab 1 - basicConfig for file, StreamHandler for terminal.
    pass


def check_service(name, url, timeout, response_time_threshold):
    # Send an HTTP GET request to the url and measure response time.
    # Return a dict with keys: name, url, status, response_time_ms, status_code
    # Status should be "UP", "DEGRADED", or "DOWN"
    # DEGRADED means it responded but slower than response_time_threshold
    # DOWN means it timed out or threw a connection error
    # HINT: use requests.get() with a timeout parameter
    # HINT: use time.time() before and after the request to measure elapsed time
    # HINT: wrap in try/except for requests.exceptions.RequestException
    pass


def generate_report(results):
    # Print a formatted health report to the terminal.
    # Show a header with the current timestamp
    # Loop through results and print each service status, url, and response time
    # Show a summary line at the bottom with total UP, DEGRADED, DOWN counts
    # HINT: use f-strings and string formatting to align columns cleanly
    pass


def main():
    # Load config
    # Set up logging
    # Loop through services in config and call check_service for each
    # Collect results into a list
    # Call generate_report with the results
    # Log each result
    # OPTIONAL: wrap in a while True loop with time.sleep for continuous monitoring
    pass


if __name__ == "__main__":
    main()