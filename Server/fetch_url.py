from googlesearch import search
def get_url(urls,query):
    search_results = list(search(query, num_results=2))  # Adjust the number as needed for number of links to open and parse the data from google searched    
    # Extract the top 3 URLs from the search results
    top_links = search_results[:2]    
    # put links in urls array
    for i, link in enumerate(top_links, start=1):
        urls.append(link)
    for i in urls:
        print("URL:", i)
    return urls