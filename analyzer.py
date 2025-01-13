import aiohttp
import asyncio
import json
import os
import logging
import http.client
from urllib.parse import urlparse

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Enable HTTP connection debugging
http.client.HTTPConnection.debuglevel = 1
logging.getLogger("aiohttp").setLevel(logging.DEBUG)


def normalize_url(url):
    """Ensure the URL has a valid scheme."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        logging.debug(f"Normalized URL: {url}")
    return url


async def analyze_headers(url, session, request_type="HEAD", retries=3):
    url = normalize_url(url)  # Normalize the URL before processing
    attempt = 0
    while attempt < retries:
        try:
            attempt += 1
            logging.debug(f"Attempting to analyze {url} (Attempt {attempt}/{retries})")
            
            if request_type.upper() == "GET":
                async with session.get(url, timeout=10) as response:
                    headers = response.headers
            else:
                async with session.head(url, timeout=10) as response:
                    headers = response.headers

            logging.info(f"Analyzing headers for: {url}")
            results = {"url": url, "headers": {}, "security_headers": []}

            # Collect headers
            for header, value in headers.items():
                logging.debug(f"{header}: {value}")
                results["headers"][header] = value

            # Security Headers Check
            security_headers = {
                "Content-Security-Policy": "Helps prevent XSS attacks by defining content sources.",
                "X-Content-Type-Options": "Prevents browsers from MIME-sniffing the content-type.",
                "X-Frame-Options": "Prevents clickjacking by restricting iframe embedding.",
                "Strict-Transport-Security": "Enforces HTTPS connections to the server.",
                "Referrer-Policy": "Controls the information sent in the Referer header.",
                "Permissions-Policy": "Controls access to browser features (formerly Feature-Policy).",
                "X-XSS-Protection": "Enables the cross-site scripting filter in browsers (deprecated but useful for older browsers).",
            }

            for header, recommendation in security_headers.items():
                if header in headers:
                    logging.info(f"[OK] {header} is present.")
                    results["security_headers"].append({"header": header, "status": "present"})
                else:
                    logging.warning(f"[MISSING] {header} is not present. Recommendation: {recommendation}")
                    results["security_headers"].append({"header": header, "status": "missing", "recommendation": recommendation})

            return results

        except asyncio.TimeoutError:
            logging.error(f"Timeout occurred for {url} (Attempt {attempt}/{retries})")
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")

    logging.error(f"All {retries} attempts failed for {url}")
    return None


def save_results_to_file(results, output_file):
    try:
        if os.path.exists(output_file):
            with open(output_file, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.extend(results)

        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)

        logging.info(f"Results saved to {output_file}")

    except Exception as e:
        logging.error(f"Error saving results to file: {e}")


async def process_multiple_urls(file_path, request_type="HEAD", output_file=None):
    try:
        with open(file_path, "r") as file:
            urls = [url.strip() for url in file.readlines()]

        async with aiohttp.ClientSession() as session:
            tasks = [analyze_headers(url, session, request_type) for url in urls]
            results = await asyncio.gather(*tasks)

        # Filter out None results (in case of errors)
        results = [result for result in results if result is not None]

        # Save results to file
        if output_file:
            save_results_to_file(results, output_file)

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")


if __name__ == "__main__":
    print("HTTP Header Analyzer - Logging and Retry Enabled")
    print("1. Analyze a single URL")
    print("2. Analyze multiple URLs from a file")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        url = input("Enter URL to analyze (e.g., https://example.com): ")
        request_type = input("Request type (HEAD or GET) [default: HEAD]: ").strip() or "HEAD"

        async def run_single_url():
            async with aiohttp.ClientSession() as session:
                result = await analyze_headers(url, session, request_type)
                if result:
                    output_file = input("Output file to save results (optional): ").strip() or None
                    if output_file:
                        save_results_to_file([result], output_file)
        asyncio.run(run_single_url())

    elif choice == "2":
        file_path = input("Enter the file path containing URLs: ").strip()
        request_type = input("Request type (HEAD or GET) [default: HEAD]: ").strip() or "HEAD"
        output_file = input("Output file to save results (optional): ").strip() or None
        asyncio.run(process_multiple_urls(file_path, request_type, output_file))

    else:
        print("Invalid choice. Exiting.")
