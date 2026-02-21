#Log Analyzer
#Parses system log files, categorizes entries by severity,and generates a summary report.

import argparse
from datetime import datetime
from collections import Counter


def parse_arguments():
    """Set up command-line arguments."""
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("--level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], help="Filter by log level")
    parser.add_argument("--keyword", help="Filter by keyword in message")
    parser.add_argument("--after", type=datetime.fromisoformat, help="Filter entries after this timestamp")
    parser.add_argument("--before", type=datetime.fromisoformat, help="Filter entries before this timestamp")
    return parser.parse_args()

def parse_log_line(line):
    """Parse a single log line into its components (timestamp, level, message)."""
    # TODO: Split the line into timestamp, level, and message
    # TODO: Return them as a dictionary
    # HINT: The format is "2026-02-16 12:00:01,194 - INFO - Monitor started."
    #       Split on " - " to get the parts
    pass


def read_log_file(filepath):
    """Read log file and return list of parsed entries."""
    # TODO: Open the file, read each line, parse it with parse_log_line()
    # TODO: Return a list of parsed entries
    # TODO: Handle FileNotFoundError
    pass


def filter_entries(entries, level=None, keyword=None, after=None, before=None):
    """Filter log entries based on criteria."""
    # TODO: Start with all entries
    # TODO: If level is set, keep only entries at that level or higher
    # TODO: If keyword is set, keep only entries whose message contains that keyword
    # TODO: If after/before is set, keep only entries within that time range
    # TODO: Return the filtered list
    pass


def generate_report(entries, filepath):
    """Generate and print the summary report."""
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