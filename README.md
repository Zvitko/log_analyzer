# Log Analyzer

A Python-based log analyzer that processes log files, categorizes log entries by severity (e.g., INFO, ERROR, WARNING), and generates a detailed summary.



## Features
- Dynamically detects and tracks log levels (e.g., INFO, ERROR, WARNING).
- Counts occurrences of each log level.
- Displays a summary of all log levels and their associated messages.
- Skips malformed log entries and logs a warning.
- Includes error handling for missing or inaccessible files.

### Running the Log Analyzer with argparse

The `LogAnalyzer` script uses Python's `argparse` module to handle command-line arguments. You can specify the log file to analyze directly from the terminal.

#### Steps to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where `log_analyzer.py` is located:
   ```bash
   - cd /path/to/log-analyzer
   - python log_analyzer.py /path/to/log.txt
