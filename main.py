from flask import Flask, render_template, request
from scanner.tech_stack_detector import detect_tech_stack
from scanner.security_header_scanner import scan_security_headers
from scanner.xss_scanner import scan_xss
from utils.report_generator import save_report
import os
from datetime import datetime

app = Flask(__name__)

# Home page (Scanner + Framework buttons)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')

        headers_result = detect_tech_stack(url)
        security_headers_result = scan_security_headers(url)
        xss_result = scan_xss(url)

        # Save report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join("reports", f"report_{timestamp}.html")
        save_report(url, headers_result, security_headers_result, xss_result, report_path)

        return render_template(
            'index.html',
            url=url,
            headers=headers_result,
            security_headers=security_headers_result,
            xss_result=xss_result,
            report_path=report_path,
            scanned=True
        )

    return render_template('index.html', scanned=False)


# Frameworks Page
@app.route('/frameworks')
def frameworks():
    return render_template('frameworks.html')


if __name__ == '__main__':
    app.run(debug=True)
