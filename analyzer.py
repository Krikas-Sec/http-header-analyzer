import requests

def analyze_headers(url):
    try:
        response = requests.head(url)
        headers = response.headers

        print(f"\nAnalyzing headers for: {url}\n")
        for header, value in headers.items():
            print(f"{header}: {value}")

        # Check and recommend security headers
        security_headers = {
            "Content-Security-Policy": "Helps prevent XSS attacks by defining content sources.",
            "X-Content-Type-Options": "Prevents browsers from MIME-sniffing the content-type.",
            "X-Frame-Options": "Prevents clickjacking by restricting iframe embedding.",
            "Strict-Transport-Security": "Enforces HTTPS connections to the server.",
            "Referrer-Policy": "Controls the information sent in the Referer header.",
            "Permissions-Policy": "Controls access to browser features (formerly Feature-Policy).",
            "X-XSS-Protection": "Enables the cross-site scripting filter in browsers (deprecated but useful for older browsers).",
        }

        print("\nSecurity Headers Check:")
        for header, recommendation in security_headers.items():
            if header in headers:
                print(f"[OK] {header} is present.")
            else:
                print(f"[MISSING] {header} is not present. Recommendation: {recommendation}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    print("HTTP Header Analyzer")
    url = input("Enter URL to analyze (e.g., https://example.com): ")
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Default to HTTPS if the scheme is missing
    analyze_headers(url)
