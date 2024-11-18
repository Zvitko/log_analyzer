import logging

class LogAnalyzer:
    def __init__(self, file_path: str):
        """Initialize the log analyzer with a file path."""
        self.file_path = file_path
        self.log_summary: dict[str, dict[str, list | int]] = {}

    def analyze_log(self):
        """Reads the log file and updates the log summary."""
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if ": " not in line:
                        logging.warning(f"Skipping malformed line: {line}")
                        continue

                    level, message = line.split(": ", 1)

                    # Add log level dynamically if not present
                    if level not in self.log_summary:
                        self.log_summary[level] = {"count": 0, "messages": []}

                    self.log_summary[level]["count"] += 1
                    self.log_summary[level]["messages"].append(message)

        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def display_summary(self):
        """Displays the log summary."""
        if not self.log_summary:
            print("No logs to display.")
            return

        print("\nLog Summary:")
        print("=" * 20)
        for level, info in self.log_summary.items():
            print(f"\n{level}: {info['count']} occurrences")
            print("Messages:")
            for message in info["messages"]:
                print(f"  - {message}")
        print("\n" + "=" * 20)

# Command Line Usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a log file.")
    parser.add_argument("file_path", help="Path to the log file")
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file_path) 
    analyzer.analyze_log()
    analyzer.display_summary()
