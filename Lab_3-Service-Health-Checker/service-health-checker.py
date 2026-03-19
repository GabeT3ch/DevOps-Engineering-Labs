# Service Health Checker - Monitors HTTP/HTTPS endpoints and reports availability and response time.
import requests
import yaml
import logging
import time


def load_config(config_path="config.yaml"):
    try:

        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"Config file {config_path} not found.")
        return None
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML config: {e}")
        return None


def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)


def check_service(name, url, timeout, response_time_threshold):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        status_code = response.status_code

        if response_time_ms > response_time_threshold:
            status = "DEGRADED"
        else:
            status = "UP"
    except requests.RequestException as e:
        logging.error(f"Error checking service {name}: {e}")
        status = "DOWN"
        response_time_ms = None
        status_code = None

    return {
        "name": name,
        "url": url,
        "status": status,
        "response_time_ms": response_time_ms,
        "status_code": status_code
    }


def generate_report(results):
    for result in results:
        response_time = f"{result['response_time_ms']:.1f} ms" if result['response_time_ms'] else "N/A"
        logging.info(f"{result['name']} - {result['status']} - {response_time}")
    up = sum(1 for r in results if r['status'] == 'UP')
    degraded = sum(1 for r in results if r['status'] == 'DEGRADED')
    down = sum(1 for r in results if r['status'] == 'DOWN')
    logging.info(f"Summary: {up} UP, {degraded} DEGRADED, {down} DOWN")


def main():
    config = load_config(config_path="config.yaml")
    if not config:
        logging.error("Failed to load configuration.")
        return

    setup_logging(config.get("log_file", "health_check.log"))

    results = []
    for service in config.get("services", []):
        result = check_service(
            name=service["name"],
            url=service["url"],
            timeout=service["timeout"],
            response_time_threshold=service["response_time_threshold"]
        )
        results.append(result)

    generate_report(results)


if __name__ == "__main__":
    main()
