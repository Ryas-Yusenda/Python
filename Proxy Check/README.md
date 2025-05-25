# Proxy Checker

A Python script to test a list of proxies and measure their response time to a target URL.

## Description

This script checks the availability and performance of HTTP/HTTPS proxies by sending requests to a target URL (default: `https://www.google.com`). It measures the response time of each proxy over multiple attempts and saves the working proxies with their average response time to a `working_proxies.json` file.

## Installation

- Ensure Python is installed on your system. [Get Python](https://www.python.org/downloads/)
- Install required dependencies:

  ```bash
  pip install requests
  ```

# Quick Start

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Prepare a `working_proxies.json` file with your list of proxies in the format.

3. Run the script:

   ```bash
   python main.py
   ```
