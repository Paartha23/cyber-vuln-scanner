from flask import Flask, render_template, request
from scanner.tech_stack_detector import detect_tech_stack
from scanner.security_header_scanner import scan_security_headers
from scanner.xss_scanner import scan_xss

app = Flask(__name__)

@app.route('/frameworks')
def frameworks():
    return render_template('frameworks.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None  # Set to None initially
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            results = {
                'url': url,
                'tech_stack': detect_tech_stack(url),
                'headers': scan_security_headers(url),
                'xss': scan_xss(url)
            }
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)

