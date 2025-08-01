import requests

def scan_security_headers(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)

        # List of important security headers
        important_headers = {
            "Content-Security-Policy": "Prevents XSS attacks",
            "Strict-Transport-Security": "Enforces HTTPS",
            "X-Frame-Options": "Prevents clickjacking",
            "X-Content-Type-Options": "Prevents MIME-sniffing",
            "Referrer-Policy": "Controls Referer header",
            "Permissions-Policy": "Restricts browser features"
        }

        results = {}
        print("\n🔐 Security Header Scan:")
        for header, purpose in important_headers.items():
            if header in response.headers:
                print(f"[✅] {header} — Present")
                results[header] = "Present"
            else:
                print(f"[❌] {header} — MISSING ({purpose})")
                results[header] = f"Missing ({purpose})"
        return results

    except requests.exceptions.RequestException as e:
        print(f"[!] Error scanning headers: {e}")
        return {"error": str(e)}
