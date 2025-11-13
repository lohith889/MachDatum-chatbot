import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# CONFIG
START_URL = "https://www.machdatum.com"
DOMAIN = "machdatum.com"
MAX_PAGES = 50   # Increase if you want deeper coverage

visited = set()
to_visit = [START_URL]

def is_internal(url):
    try:
        host = urlparse(url).netloc
        return DOMAIN in host
    except:
        return False

def clean_url(url):
    # Remove fragments, query strings, trailing slashes
    url = url.split("#")[0]
    url = url.split("?")[0]
    return url.rstrip("/")

all_urls = []

print("Crawling started \n")

while to_visit and len(visited) < MAX_PAGES:
    current = to_visit.pop(0)
    current = clean_url(current)

    if current in visited:
        continue

    print(f"FETCHING: {current}")
    visited.add(current)
    all_urls.append(current)

    try:
        resp = requests.get(current, timeout=10)
        if resp.status_code != 200:
            continue

        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a")

        for tag in links:
            href = tag.get("href")

            if not href:
                continue

            full_url = clean_url(urljoin(current, href))

            if is_internal(full_url) and full_url not in visited:
                to_visit.append(full_url)

    except:
        continue

print("\n\n--- FINAL URL LIST (To Feed Into Gemini) ---\n")
for url in all_urls:
    print(url)

print(f"\nTotal URLs collected: {len(all_urls)}")
