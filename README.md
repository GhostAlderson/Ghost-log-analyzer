Ghost Log Analyzer

A beginner-built Python project focused on HTTP request logging and basic log analysis.

«Status: Work in Progress (WIP)

This project is part of my cybersecurity learning journey. It is being developed step by step to practice Python, HTTP, logging, and basic security-related analysis. The code is still evolving, and improvements will be added over time.»

About

Ghost Log Analyzer is a small educational project that combines a basic HTTP server with a simple log analysis component.

The goal is to understand how HTTP requests can be recorded and how log data can be processed to extract useful information.

This is a learning project, not a production-ready security tool.

Current Features

- Basic HTTP request handling using Python.
- Logging request information, including HTTP methods, paths, and client IP addresses.
- Appending request records to a local log file.
- Reading log entries and counting requests by IP address.
- Basic local testing with HTTP requests.

Project Structure

Ghost-Log-Analyzer/
├── main.py
├── analyze-logs.py
├── README.md
└── .gitignore

The "ghost.log" file is generated locally and is intentionally excluded from version control.

Requirements

- Python 3
- A terminal environment, such as Termux
- "curl" for basic HTTP testing

How It Works

1. HTTP Server

"main.py" runs a local HTTP server on "127.0.0.1:8082" and records incoming request information in "ghost.log".

2. Log Analyzer

"analyze-logs.py" runs a separate local HTTP server on "127.0.0.1:8083".

When it receives a supported request, it reads the log file and counts recorded requests by client IP address.

Current Limitations

- The project has only undergone basic local testing.
- The analyzer currently focuses on counting requests by IP address.
- Request methods, endpoints, and HTTP status codes are not yet comprehensively analyzed.
- Error handling and malformed log entries need further testing.
- The implementation may contain limitations and bugs that will be addressed during development.

Roadmap

Planned improvements include:

- Counting requests by HTTP method and endpoint.
- Recording and analyzing HTTP status codes.
- Improving malformed-log handling and error reporting.
- Adding more local test scenarios.
- Expanding the analysis features.
- Improving the overall reliability of the tool.

Security Notice

This project is intended for educational use in a local, authorized environment.

Do not expose the development servers to untrusted networks. Do not publish logs containing sensitive information, credentials, session identifiers, or private user data.

Author

Ghost

Learning cybersecurity through hands-on Python projects.

License

No license has been selected yet.
