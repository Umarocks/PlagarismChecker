from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Define the search query
query = "The company said the new phones' titanium frame and aluminum substructure aren't contributing to the issue, and that they dissipate heat better than the stainless steel used in prior Pro models"

# Perform the Google search and get search results
search_results = list(search(query, num_results=5))  # Adjust the number as needed

# Extract the top 5 URLs from the search results
top_links = search_results[:5]
urls = []
# put linkes in urls array
for i, link in enumerate(top_links, start=1):
    urls.append(link)

for i in urls:
    print("URL:", i)

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

# Parse and print the data from each URL
for i, url in enumerate(urls, start=1):
    print(f"Processing URL {i}: {url}")
    soup = parse_url(url)
    if soup:
        headings_and_paragraphs = [tag.text.strip() for tag in soup.find_all([ 'p', 'a'])]
        # Extract text within a tags
        filtered_headings_and_paragraphs = [text for text in headings_and_paragraphs if len([word for word in text.split() if word.strip()]) > 4]
        output_string = ' '.join(filtered_headings_and_paragraphs)
        # Print the extracted text
        print("Headings:", output_string)
     
        
    print("\n" + "-" * 40 + "\n")  # Separator between URLs

