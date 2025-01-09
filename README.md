# HTTP Header Analyzer

A simple Python tool to analyze HTTP headers for common security issues.

## Features
- Analyzes HTTP headers for the presence of key security headers:
  - Content-Security-Policy
  - X-Content-Type-Options
  - X-Frame-Options
  - Strict-Transport-Security
- Displays all headers for a given URL.
- Highlights missing security headers.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/http-header-analyzer.git
   cd http-header-analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python analyzer.py
   ```

2. Enter the URL you want to analyze when prompted.

## Example Output
For the URL `https://example.com`, the output might look like:
```plaintext
Analyzing headers for: https://example.com
server: nginx
content-type: text/html
...

Security Headers Check:
[OK] Content-Security-Policy is present.
[MISSING] X-Content-Type-Options is not present.
...
```

## Roadmap
- Add support for analyzing additional security headers.
- Provide recommendations for missing headers.
- Support bulk URL analysis.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, contact me at `krikas@temphack.org` or visit [temphack.org](https://temphack.org).
