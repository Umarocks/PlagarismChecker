from bs4 import BeautifulSoup
from googlesearch import search
import requests
# Function to fetch and parse a URL
def parse_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {str(e)}")
        return None
    