import requests
from bs4 import BeautifulSoup

def detect_tech_stack(url):
    tech_stack = []

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)

        # Server header
        server = response.headers.get("Server")
        if server:
            tech_stack.append(f"Server: {server}")

        # X-Powered-By header
        powered_by = response.headers.get("X-Powered-By")
        if powered_by:
            tech_stack.append(f"Powered By: {powered_by}")

        # Technologies from meta tags
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tags = soup.find_all("meta")
        for tag in meta_tags:
            if tag.get("name") and tag.get("content"):
                name = tag["name"].lower()
                content = tag["content"].lower()
                if "generator" in name or "framework" in name or "cms" in content:
                    tech_stack.append(f"Meta: {tag['content']}")

        # Add fallback if nothing was detected
        if not tech_stack:
            tech_stack.append("No identifiable technologies detected.")

    except requests.exceptions.RequestException as e:
        tech_stack.append(f"Error: {str(e)}")

    return tech_stack
