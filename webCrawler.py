from googlesearch import search
import requests
from bs4 import BeautifulSoup
import gensim
from gensim import corpora
from gensim import similarities
import nltk
# nltk.download('punkt')
input_string="The company said the new phones' titanium frame and aluminum substructure aren't contributing to the issue, and that they dissipate heat better than the stainless steel used in prior Pro models.Soccer is played with a round ball that can be kicked and headed. American football, however, is more of a rugby type game in which the oblong shaped ball is thrown and passed as well as kicked."
# Define the search query
query = []
urls = []
reference_documents=[]
sentences = []
score_tracker=0
score = [0] 
# Function to tokenize and generate n-grams from a given text
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = " ".join(tokens[i:i + n])
        ngrams.append(ngram)
    return ngrams

# Function to calculate Jaccard similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Function to check for plagiarism using n-grams analysis
def detect_plagiarism(source_text, suspicious_text, n=3, threshold=0.5):
    source_ngrams = set(generate_ngrams(source_text, n))
    suspicious_ngrams = set(generate_ngrams(suspicious_text, n))
    similarity = jaccard_similarity(source_ngrams, suspicious_ngrams)
    score[score_tracker]=max(score[score_tracker],similarity)

def compute_plagarism():
    global score_tracker  # Assuming score_tracker is defined somewhere outside this function.
    sus_sentence=query[score_tracker]
    # print("SUS SENTENCE:",sus_sentence)    
    # print(query)
    source_text = sus_sentence
    for sentence in sentences:
        suspicious_text = sentence
        # print(suspicious_text)
        is_plagiarism = detect_plagiarism(source_text, suspicious_text, n=3, threshold=0.5)
        # if is_plagiarism:
        #     print("Plagiarism detected.")
        # else:
        #     print("No plagiarism detected.")     
    score_tracker += 1  # Increment score_tracker for each sus_sentence
    score.append(0)
    # print(score)
    # print(score_tracker)

   

def get_url():
    # Perform the Google search and get search results
    for sus_sentence in query:
        search_results = list(search(sus_sentence, num_results=2))  # Adjust the number as needed

        # Extract the top 5 URLs from the search results
        top_links = search_results[:2]
        
        # put linkes in urls array
        for i, link in enumerate(top_links, start=1):
            urls.append(link)

        # for i in urls:
        #     print("URL:", i)
        string_cleaning()
        urls.clear()

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

def string_cleaning():
    for i, url in enumerate(urls, start=1):
        # print(f"Processing URL {i}: {url}")
        soup = parse_url(url)
        if soup:
            headings_and_paragraphs = [tag.text.strip() for tag in soup.find_all([ 'p', 'a'])]
            # Extract text within a tags
            filtered_headings_and_paragraphs = [text for text in headings_and_paragraphs if len([word for word in text.split() if word.strip()]) > 4]
            # print(filtered_headings_and_paragraphs)
            for i in filtered_headings_and_paragraphs:
                if '.' in i:
                    # Split the string based on periods
                    substrings = i.split('.')
                    
                    # Remove empty strings (if any)
                    substrings = [substring.strip() for substring in substrings if substring.strip()]
                    
                    # Extend the final list with the split substrings
                    sentences.extend(substrings)
                else:
                    # No period found, append the whole string
                    sentences.append(i)
            # Print the array of sentences
            # for sentence in sentences:
            #     print(sentence)
    
        # print("\n" + "-" * 40 + "\n")  # Separator between URLs
    compute_plagarism()

def filtering(input_string , query):
    # Split the input string into an array of strings using periods as the delimiter
    sentences = input_string.split(".")

    # Remove leading/trailing spaces and empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # Print the resulting array of sentences
    query.extend(sentences)

def average_without_last_element(arr):
    sum_for_avg=0
    for i in range(0,(len(score)-1)):
        sum_for_avg+=i
    average=sum_for_avg/(len(score)-1)
    return average

filtering(input_string,query)
get_url()   
print("Plagarism is : ",average_without_last_element(score)*100,"%")
    
