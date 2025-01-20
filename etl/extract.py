import requests
from bs4 import BeautifulSoup

def fetch_live_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract specific data from HTML
        data = extract_data(soup)
        return data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def extract_data(soup):
    # Example: Extract data from table or div
    data = []
    for item in soup.select("div.item"):
        title = item.select_one("h2.title").text
        value = item.select_one("span.value").text
        data.append({"title": title, "value": value})
    return data