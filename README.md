# HTTP Header Analyzer

A powerful Python tool to analyze HTTP headers for common security issues and evaluate a website's HTTP configuration. The tool supports both single and bulk URL analysis, providing detailed reports and recommendations.

---

## Features

- **Analyze HTTP Headers**:
  - Scans for the presence of key security headers:
    - `Content-Security-Policy`
    - `X-Content-Type-Options`
    - `X-Frame-Options`
    - `Strict-Transport-Security`
    - `Referrer-Policy`
    - `Permissions-Policy`
    - `X-XSS-Protection`
  - Displays all HTTP headers for a given URL.
  - Highlights missing security headers and provides actionable recommendations.

- **Bulk URL Analysis**:
  - Analyze multiple URLs from a file, with results saved to a JSON file.

- **Error Handling and Logging**:
  - Logs errors and detailed debug information to a `debug.log` file for later review.
  - Retries failed requests up to 3 times to ensure reliability.

- **Asynchronous Requests**:
  - Uses `aiohttp` and `asyncio` for fast and efficient bulk analysis.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/USERNAME/http-header-analyzer.git
cd http-header-analyzer
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Script
```bash
python analyzer.py
```

### Options:
1. **Analyze a Single URL**:
   - Enter a URL when prompted. Example: `https://example.com`.

2. **Analyze Multiple URLs**:
   - Prepare a file containing URLs (one per line). Example `urls.txt`:
     ```
     https://example.com
     google.com
     temphack.org
     ```
   - Specify the file path when prompted.

3. **Output Results**:
   - Results for bulk analysis can be saved to a JSON file for later review.

---

## Example Output

For the URL `https://example.com`, the output might look like:

```plaintext
Analyzing headers for: https://example.com
server: nginx
content-type: text/html

Security Headers Check:
[OK] Content-Security-Policy is present.
[MISSING] X-Content-Type-Options is not present. Recommendation: Prevents browsers from MIME-sniffing the content-type.
[MISSING] Referrer-Policy is not present. Recommendation: Controls the information sent in the Referer header.
...
```

---

## Logging

- **Log File**: `debug.log`
  - Contains detailed debug and error information for each request, including retries and any issues encountered.
  - Example:
    ```
    2025-01-13 20:00:00 - DEBUG - Normalized URL: https://google.com
    2025-01-13 20:00:01 - INFO - Analyzing headers for: https://google.com
    2025-01-13 20:00:01 - ERROR - Timeout occurred for https://temphack.org (Attempt 1/3)
    ```

---

## Roadmap

- Add more security header checks and recommendations.
- Support customizable request settings (e.g., custom headers, user agents).
- Implement a graphical user interface (GUI) for easier usage.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or support:
- **Email**: [krikas@temphack.org](mailto:krikas@temphack.org)
- **Website**: [temphack.org](https://temphack.org)
