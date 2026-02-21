# Log Analyzer - Parses system log files, categorizes entries by severity, and generates a summary report.

import argparse
import logging
from datetime import datetime
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_arguments():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("--level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="Filter by log level")
    parser.add_argument("--keyword", help="Filter by keyword in message")
    parser.add_argument("--after", type=datetime.fromisoformat, help="Filter entries after this timestamp")
    parser.add_argument("--before", type=datetime.fromisoformat, help="Filter entries before this timestamp")
    return parser.parse_args()


def parse_log_line(line):
    # Parse a single log line into its components (timestamp, level, message)
    try:
        parts = line.split(" - ")
        return {
            "timestamp": datetime.strptime(parts[0].strip(), "%Y-%m-%d %H:%M:%S,%f"),
            "level": parts[1].strip(),
            "message": parts[2].strip()
        }
    except (IndexError, ValueError):
        return None


def read_log_file(filepath):
    # Read log file and return list of parsed entries with error handling for file not found
    try:
        with open(filepath, "r") as log_file:
            return [entry for entry in [parse_log_line(line) for line in log_file] if entry is not None]
    except FileNotFoundError:
        logger.error(f"Log file '{filepath}' not found.")
        return []
    except PermissionError:
        logger.error(f"Permission denied reading '{filepath}'.")
        return []


def filter_entries(entries, level=None, keyword=None, after=None, before=None):
    # Filter log entries based on criteria.
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
    # Generate and print the summary report.
    if not entries:
        print(f"No entries found in {filepath} matching the given filters.")
        return

    counts = Counter(e["level"] for e in entries)
    first_entry = entries[0]["timestamp"]
    last_entry = entries[-1]["timestamp"]
    common_messages = Counter(e["message"] for e in entries).most_common(5)

    print(f"\nLog Analysis Report for {filepath}")
    print(f"{'='*50}")
    print(f"Total entries: {len(entries)}")
    print(f"Time range: {first_entry} to {last_entry}")
    print("\nEntries by level:")
    for level, count in counts.items():
        print(f"  {level}: {count}")
    print("\nMost frequent messages:")
    for message, count in common_messages:
        print(f"  ({count}x) {message}")


def main():
    args = parse_arguments()
    entries = read_log_file(args.log_file)
    filtered = filter_entries(entries, level=args.level, keyword=args.keyword, after=args.after, before=args.before)
    generate_report(filtered, args.log_file)


if __name__ == "__main__":
    main()