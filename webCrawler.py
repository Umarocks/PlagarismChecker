from googlesearch import search
import requests
from bs4 import BeautifulSoup
import gensim
from gensim import corpora
from gensim import similarities
import nltk
# nltk.download('punkt')
input_string="Many in Australia, New Zealand, and Ireland call association football soccer, likely as a way to distinguish it from Australian rules football and Gaelic football, which are commonly referred to just as football in those places—just as Americans call American football simply football."
# Define the search query
query = []
urls = []
reference_documents=[]
sentences = []
score_tracker=0
score = [0] 

def detect_plagiarism(source_text, suspicious_text, n=3, threshold=0.5):
    # source_ngrams = set(generate_ngrams(source_text, n))
    # suspicious_ngrams = set(generate_ngrams(suspicious_text, n))
    # similarity = jaccard_similarity(source_ngrams, suspicious_ngrams)
    # score[score_tracker]=max(score[score_tracker],similarity)
    return 0

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
                    substrings = i.split(".")
                    
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
    # Remove leading/trailing spaces and empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # Print the resulting array of sentences
    query.extend(sentences)

def average_without_last_element(arr):
    if len(arr) <= 1:
        return 0  # Handle the case where the array is empty or has only one element
    
    # Sum all elements except the last one
    total_sum = sum(arr[:-1])
    
    # Calculate the average
    average = total_sum / (len(arr) - 1)
    
    return average



# Example
sequence1 = "Many in Australia, New Zealand, and  call  football , likely as a way to  it Ireland  from Australian rules football  Gaelic football, which are commonly  association to just as football in those places—just as Americans call American football simply football."
sequence2 = "If you’re reading this in the US or Canada, you’re likely familiar with the sport of soccer. But, if you’re reading this pretty much anywhere else, then you probably know the same game rules and call it football. What’s the difference?How did we end up with two names, football and soccer, for the same sport?Let’s start in England in the 1800s. Young men, especially at boarding schools, played a number of versions of moving a ball (with hands or feet) across an opponent’s goal. At Rugby School, for instance, they played a version that allowed for use of the hands; at Eton College, only feet were permitted.So, in 1863 in London, a Football Association (the world’s first) was formed to standardize the rules. Two codes resulted from it: rugby football, after Rugby School, and association football, after that newly formed association.Keep Learning New Words Every Day!Get the Word of The Day delivered straight to your inbox!yourname@email.comWhere does the word soccer come from?Now, around the 1870s, students, especially at Oxford University, were fond of a playful slang practice where they shortened words and added –er to their end. Breakfast, for instant, became brekker. Rugby? Rugger. Football? Footer.The association in association football was also shortened to soccer. This clips off the first and last three syllables of association, leaving –soc-, onto which that chummy –er was added, yielding soccer. The term is first recorded as socker in 1891. Footer is slightly older, found in that fateful year of 1863.What is the origin of American football?But, what about that other football that people in the US bring to the Super Bowl? American football (a term recorded in the 1870s) is based on rugby and had already taken off by the time association football became popular in the US.For whatever reason, the name soccer stuck for association football and football for the gridiron sport. In fact, the governing body for soccer in the US was called the United States Soccer Football Association until 1974.How many football fans know the origins of the terms used in the American sport? Learn about quarterback and more, here.Does anyone else around the world call football soccer?Americans and Canadians aren’t alone, however, in calling the sport soccer. Many in Australia, New Zealand, and Ireland call association football soccer, likely as a way to distinguish it from Australian rules football and Gaelic football, which are commonly referred to just as football in those places—just as Americans call American football simply football.So, the next time a British person thumbs their nose at you for calling football soccer, you can let them know that soccer was a UK original! And, if you’re having trouble keeping all these names straight, take a page from Spanish and call it … fútbol!"
alignment1, alignment2, score = smith_waterman(sequence1, sequence2)
# Example
distance = levenshtein_distance(alignment1, alignment2)
print(f"Levenshtein Distance between '{alignment1}' and '{alignment2}': {distance}")
a = (len(alignment2)-distance)
plag=0;
if(a>0):
    plag = (a*100)/len(alignment1)
print(plag)
print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
print("Alignment Score:", score)    

filtering(input_string,query)
get_url()   
print(score)
print(query)
# print(sentences)
print(average_without_last_element(score))
print("Plagarism is : ",average_without_last_element(score)*100,"%")
    