#Log Analyzer Parses system log files, categorizes entries by severity,and generates a summary report.

import argparse
from datetime import datetime
from collections import Counter


def parse_arguments():
    #Set up command-line arguments
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("--level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="Filter by log level")
    parser.add_argument("--keyword", help="Filter by keyword in message")
    parser.add_argument("--after", type=datetime.fromisoformat, help="Filter entries after this timestamp")
    parser.add_argument("--before", type=datetime.fromisoformat, help="Filter entries before this timestamp")
    return parser.parse_args()

def parse_log_line(line):
    #Parse a single log line into its components (timestamp, level, message)
    parts = line.split((" - "))
    return {
            "timestamp": datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S,%f"),
            "level": parts[1],
            "message": parts[2]
        }

def read_log_file(filepath):
    #Read log file and return list of parsed entries with error handling for file not found
    try:
        with open(filepath, "r") as log_file:
            return [parse_log_line(line) for line in log_file]
    except FileNotFoundError:
        print(f"Error: Log file '{filepath}' not found.")
        return []
    


def filter_entries(entries, level=None, keyword=None, after=None, before=None):
    #Filter log entries based on criteria.
    results = entries
    if level is not None:
        level_order = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
        results = [e for e in results if level_order[e["level"]] >= level_order[level]]
    if keyword is not None:
        results = [e for e in results if keyword.lower() in e["message"].lower()]
    if after is not None:
        results = [e for e in results if e["timestamp"] >= after]
    if before is not None:
        results = [e for e in results if e["timestamp"] <= before]
    return results


    


def generate_report(entries, filepath):
    #Generate and print the summary report.

 
    # TODO: Count entries by log level
    # TODO: Find the time range (first and last entry)
    # TODO: Find the most frequent messages
    # TODO: Print a formatted report
    # HINT: collections.Counter is useful for counting
    pass


def main():
    """Main function."""
    # TODO: Parse arguments
    # TODO: Read the log file
    # TODO: Filter entries based on arguments
    # TODO: Generate the report
    pass


if __name__ == "__main__":
    main()