from googlesearch import search
import requests
from bs4 import BeautifulSoup
import gensim
from gensim import corpora
from gensim import similarities
import nltk
# nltk.download('punkt')
from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import gensim
from gensim import corpora
from gensim import similarities
import nltk
from flask import Flask, render_template, jsonify, request  
import string

app = Flask(__name__)

# ... (your existing code for functions like generate_ngrams, detect_plagiarism, average_without_last_element, etc.)
query = []
urls = []
reference_documents = []
sentences = []
score_tracker = 0
score = [0]



# Function to calculate Jaccard similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if(len(intersection)==0 or len(union)==0):
        return 
    return (len(intersection) / len(union))

# Function to tokenize and generate n-grams from a given text
def generate_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = " ".join(tokens[i:i + n])
        ngrams.append(ngram)
    return ngrams

# Function to check for plagiarism using n-grams analysis
def detect_plagiarism(source_text, suspicious_text, n, threshold):
    source_ngrams = set(generate_ngrams(source_text, n))
    suspicious_ngrams = set(generate_ngrams(suspicious_text, n))
    similarity = jaccard_similarity(source_ngrams, suspicious_ngrams)
    if(similarity!=0):
        print(score[score_tracker]," SCORE PER SENTENCE ",similarity)
    score[score_tracker]=max(score[score_tracker],similarity)

def compute_plagarism():
    global score_tracker  # Assuming score_tracker is defined somewhere outside this function.
    sus_sentence=query[score_tracker]
    source_text = sus_sentence
    for sentence in sentences:
        suspicious_text = sentence
        is_plagiarism = detect_plagiarism(source_text, suspicious_text, 3, threshold=0.5)    
    score_tracker += 1  
    score.append(0)



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

def clean_text(input_texts):
    # Create a translation table to remove punctuation marks
    translator = str.maketrans('', '', string.punctuation)  
    # Remove punctuation marks and convert to lowercase for each string in the array
    cleaned_texts = []
    for text in input_texts:
        cleaned_text = text.replace("\n", "").replace("\t", "").replace("\r", "")
        cleaned_text = text.translate(translator).lower()
        cleaned_texts.append(cleaned_text)
    return cleaned_texts

def string_cleaning():
    for i, url in enumerate(urls, start=1):
        soup = parse_url(url)
        if soup:
            headings_and_paragraphs = [tag.text.strip() for tag in soup.find_all([ 'p', 'a'])]
            # Extract text within a tags
            filtered_headings_and_paragraphs = [text for text in headings_and_paragraphs if len([word for word in text.split() if word.strip()]) > 4]
            for i in filtered_headings_and_paragraphs:
                if '.' in i:
                    # Split the string based on periods
                    substrings = i.split('.')  
                    # Remove empty strings (if any)
                    substrings = [substring.strip() for substring in substrings if substring.strip()]
                    # Remove newline characters and citations
                    substrings = [substring for substring in substrings if not (substring.startswith('[[') and substring.endswith(']'))]
                    # Extend the final list with the split substrings
                    sentences.extend(substrings)
                else:
                    # Remove newline characters and citations
                    i = i.strip()
                    i = i.strip('[[]]')     
                    # No period found, append the whole string
                    sentences.append(i)
            global cleaned_textss 
            cleaned_textss= clean_text(sentences)          
    compute_plagarism()
    cleaned_textss.clear()

def get_url():
    # Perform the Google search and get search results
    for sus_sentence in query:
        search_results = list(search(sus_sentence, num_results=4))  # Adjust the number as needed
        # Extract the top 5 URLs from the search results
        top_links = search_results[:2]      
        # put linkes in urls array
        for i, link in enumerate(top_links, start=1):
            urls.append(link)
        string_cleaning()
        urls.clear()
    

def average_without_last_element(arr):
    if len(arr) <= 1:
        return 0  # Handle the case where the array is empty or has only one element
    # Sum all elements except the last one
    total_sum = sum(arr[:-1])
    # Calculate the average
    average = total_sum / (len(arr) - 1)
    
    return average

def filtering(input_string , query):
    # Split the input string into an array of strings using periods as the delimiter
    sentences = input_string.split(".")
    # Remove leading/trailing spaces and empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    temp_sentences=clean_text(sentences)
    query.extend(temp_sentences)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_plagiarism', methods=['POST'])  # Specify the POST method
def calculate_plagiarism():
    global score_tracker
    # Get the input text from the JSON data sent by the client
    input_text = request.json.get('input_text')
    # Set input_string to the input text
    input_string = input_text
    query.clear()
    sentences.clear()     
    urls.clear()
    reference_documents.clear()
    score_tracker = 0
    score.clear()
    score.append(0)
    filtering(input_string,query)
    get_url()   
    # Calculate the average without the last element
    average_score = average_without_last_element(score) * 100
    print(score)
    return jsonify({'average_score': average_score})

if __name__ == '__main__':
    app.run(debug=True)










