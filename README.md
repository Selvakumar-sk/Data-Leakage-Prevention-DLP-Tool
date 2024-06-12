****Log Analysis Tool****
This Log Analysis Tool is a Python script designed to parse, analyze, and extract insights from web server log files. It helps identify patterns, anomalies, and security issues by processing logs and providing statistics on IP addresses, requested URLs, status codes, and data transferred.

**Features**
Parse log files and extract relevant information.
Convert log data into a pandas DataFrame for easy manipulation.
Analyze logs to find the top IP addresses, requested URLs, status code distribution, and total data transferred.
Simple and extendable code to fit specific log formats and analysis needs.

**Requirements**
Python 3.x
pandas library
Installation

Clone the repository:
```sh
git clone https://github.com/yourusername/log-analysis-tool.git
cd log-analysis-tool
```

Install the required libraries:
```sh
pip install pandas
```

Usage
1. Place your log file in the same directory as the script or specify the path to your log file in the script.
2. Run the script:
```sh
python log_analyzer.py
```
3. The script will parse the log file, convert it to a DataFrame, and print the analysis results to the console.
