#  Cyber Vuln Scanner

This is a **simple web vulnerability scanner** that I built using **Python and Flask**. It allows users to enter a website URL and scans it for:

-  Technology stack used by the site  
-  Security headers  
-  Reflected XSS (Cross-Site Scripting) vulnerabilities  

It has a clean, modern UI with animated backgrounds and interactive cards. I created this project to practice web security concepts and also improve my Flask + frontend development skills.

---

##  What I Used

###  Tech

- **Python 3**
- **Flask** (backend web framework)
- **HTML/CSS + JavaScript** (for frontend)
- **Particles.js** (for animated background)
- **Modern UI styles** (glassmorphism, hover effects)

###  Functionality

- `tech_stack_detector.py`: Gets server info from HTTP headers  
- `security_header_scanner.py`: Checks for important security headers like CSP, X-Frame-Options, etc.  
- `xss_scanner.py`: Injects payloads to test for reflected XSS  
- `report_generator.py`: (utility) Helps in formatting the scan results  
- Styled pages using `index.html`, `frameworks.html`, etc.

---



##  How to Run the Project

Make sure Python 3 is installed. Then:

```bash
# Clone the repository
git clone https://github.com/Paartha23/cyber-vuln-scanner.git
cd cyber-vuln-scanner

# Install required packages
pip install -r requirements.txt

# Start the Flask app
python app.py
