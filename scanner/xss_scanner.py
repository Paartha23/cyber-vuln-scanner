import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Common XSS test payload
XSS_PAYLOAD = "<script>alert('XSS')</script>"

def is_reflected(response_text, payload):
    return payload in response_text

def test_xss(url):
    print("\n🧪 XSS Scanner:")

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if not query_params:
        print("[!] No query parameters found. XSS scanner works only on URLs like ?q=search")
        return

    vulnerable = False

    # Inject payload into each parameter
    for param in query_params:
        original_value = query_params[param][0]
        query_params[param] = XSS_PAYLOAD

        # Build new URL with injected payload
        new_query = urlencode(query_params, doseq=True)
        new_url = urlunparse(parsed_url._replace(query=new_query))

        print(f"[*] Testing: {new_url}")

        try:
            response = requests.get(new_url)
            if is_reflected(response.text, XSS_PAYLOAD):
                print(f"[❌] Potential XSS vulnerability in parameter: {param}")
                vulnerable = True
            else:
                print(f"[✅] Parameter '{param}' appears safe.")
        except Exception as e:
            print(f"[!] Error scanning parameter '{param}': {e}")

        # Reset value for next param
        query_params[param] = original_value

    if not vulnerable:
        print("[+] No reflected XSS detected.")

def scan_xss(url):
    # your logic...
    print("[+] No reflected XSS detected.")
