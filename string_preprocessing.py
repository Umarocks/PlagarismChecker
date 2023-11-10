from parsing import parse_url

def filtering(input_string , query):
    # Remove leading/trailing spaces and empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # Print the resulting array of sentences
    query.extend(sentences)
    
# Parse and print the data from each URL
def string_cleaning(url,result_string):
    sentences=[]
    substrings=[]
    # for i, url in enumerate(urls, start=1):
    print(f"Processing URL {url}: {url}")
    soup = parse_url(url)
    if soup:
        headings_and_paragraphs = [tag.text.strip() for tag in soup.find_all([ 'p','h1','h2'])]
        # # Extract text within certain HTML tags
        # # print(filtered_headings_and_paragraphs)
        for i in headings_and_paragraphs:
        #     # Remove empty strings (if any)
            substrings = [substring.strip() for substring in substrings if substring.strip()]                     
        #     # Extend the final list with the split substrings
            sentences.extend(substrings)

        #     # No period found, append the whole string
            sentences.append(i)
        # # Print the array of sentences
        # # for sentence in sentences:
            
        # #     print(sentence)
    print("\n" + "-" * 40 + "\n")  # Separator between URLs
    result_string = ''.join(sentences)    
    # print("RESULT STRING OF THIS URL IS :------"+result_string)
    return result_string