#System Resource Monitor Monitors CPU, memory, and disk usage on the local machine.
#Logs readings and alerts when thresholds are exceeded.


from logging import config
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
    config = load_config()
    setup_logging(config['log_file'])
    logging.info("Monitor started.")

    try:
        while True:
            metrics = get_system_metrics()
            logging.info(f"CPU: {metrics['cpu_percent']}% | Memory: {metrics['memory_percent']}% | Disk: {metrics['disk_percent']:.1f}%")
            alerts = check_thresholds(metrics, config['thresholds'])
            for alert in alerts:
                logging.warning(alert)
            time.sleep(load_config()['interval_seconds'])
    except KeyboardInterrupt:
        logging.info("Monitor stopped.")


if __name__ == "__main__":
    main()
    