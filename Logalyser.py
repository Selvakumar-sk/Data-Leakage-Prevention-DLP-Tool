import pandas as pd
import re
from collections import Counter
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.data = []

    def parse_log(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                self.data.append(self.parse_line(line))

    def parse_line(self, line):
        # This regex will match common log formats. You might need to adjust it for your specific log format.
        regex = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d+) (?P<size>\d+|-)'
        match = re.match(regex, line)
        if match:
            return match.groupdict()
        return None

    def convert_to_dataframe(self):
        self.df = pd.DataFrame([entry for entry in self.data if entry])
        self.df['datetime'] = pd.to_datetime(self.df['datetime'], format='%d/%b/%Y:%H:%M:%S %z')
        self.df['size'] = self.df['size'].replace('-', 0).astype(int)

    def analyze(self):
        print("Top 10 IP addresses:")
        print(self.df['ip'].value_counts().head(10))

        print("\nTop 10 requested URLs:")
        self.df['request_url'] = self.df['request'].apply(lambda x: x.split()[1])
        print(self.df['request_url'].value_counts().head(10))

        print("\nStatus code distribution:")
        print(self.df['status'].value_counts())

        print("\nTotal data transferred (in bytes):")
        print(self.df['size'].sum())

    def run(self):
        self.parse_log()
        self.convert_to_dataframe()
        self.analyze()

if __name__ == "__main__":
    log_file = '\path\to\log\file'  # Replace with your log file path
    analyzer = LogAnalyzer(log_file)
    analyzer.run()
