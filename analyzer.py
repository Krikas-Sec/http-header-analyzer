import requests

def analyze_headers(url):
    try:
        response = requests.head(url)
        headers = response.headers

        print(f"Analyzing headers for: {url}")
        for header, value in headers.items():
            print(f"{header}: {value}")

        #Check security headers
        security_headers = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Option",
            "Strict-Transport-Security"
        ]
        print("\nSecurity Headers Check:")
        for header in security_headers:
            if header in headers:
                print(f"[OK] {header} is present.")
            else:
                print(f"[MISSING] {header} is not present")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter URL to analyze: ")
    analyze_headers(url)