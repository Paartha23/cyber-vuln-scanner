import os
from datetime import datetime

def save_report(url, headers_result, security_headers_result, xss_result, report_path=None):
    if not report_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join("reports", f"report_{timestamp}.html")

    os.makedirs("reports", exist_ok=True)

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(f"<html><head><title>Scan Report</title></head><body>")
        file.write(f"<h1>Scan Report for {url}</h1>")

        file.write("<h2>Tech Stack Detection</h2><ul>")
        for line in headers_result:
            file.write(f"<li>{line}</li>")
        file.write("</ul>")

        file.write("<h2>Security Headers</h2><ul>")
        for line in security_headers_result:
            file.write(f"<li>{line}</li>")
        file.write("</ul>")

        file.write("<h2>XSS Scan</h2><ul>")
        for line in xss_result:
            file.write(f"<li>{line}</li>")
        file.write("</ul>")

        file.write("</body></html>")

    print(f"✅ HTML report saved to: {report_path}")
    return report_path
