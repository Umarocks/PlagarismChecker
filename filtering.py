import string
import re
from unidecode import unidecode

STOPWORDS = set(['the', 'a', 'an', 'and', 'or', 'of', 'to', 'is', 'are', 'in', 'that', 'it', 'this', 'for', 'on', 'with', 'as', 'be', 'was', 'by', 'if', 'has', 'have', 'had', 'at', 'from', 'but', 'not', 'about', 'so', 'than', 'then', 'too', 'very', 'can', 'could', 'would', 'should', 'will', 'shall', 'may', 'might', 'must', 'do', 'does', 'did', 'done', 'doing', 'dont', 'doesnt', 'didnt', 'doing', 'im', 'ive', 'youre', 'youve', 'theyre', 'theyve', 'weve', 'werent', 'arent', 'isnt', 'wasnt', 'wont', 'cant', 'couldnt', 'wouldnt', 'shouldnt', 'mustnt', 'havent', 'hasnt', 'hadnt', 'thats', 'whats', 'whos', 'wheres', 'whens', 'whys', 'hows', 'whats', 'whos', 'wheres', 'whens', 'whys', 'hows', 'whom', 'who', 'where', 'when', 'why', 'how', 'what', 'which', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever',
'whoever', 'whomever', 'whose', 'whom', 'who', 'where', 'when', 'why', 'how', 'what', 'which', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever', 'whoever', 'whomever', 'whose', 'whomever', 'whichever'])

def preprocessing(text):
    text = text.lower()
    # remove punctuation
    cleaned_text = re.sub(r'(?<!\d)\.(?!\d)|[^\w\s.]', '', text)
    # remove numbers
    text = re.sub(r'\d+', '', text)
    # remove common words
    # text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    # remove extra spaces
    text = text.replace("\n", "").replace("\t", "").replace("\r", "")
    # text = re.sub(r'\s+', ' ', text).strip()
    # no accents
    text = unidecode(text)
    return text
# def clean_text(input_texts):
#     # Create a translation table to remove punctuation marks
#     translator = str.maketrans('', '', string.punctuation)  
#     # Remove punctuation marks and convert to lowercase for each string in the array
#     cleaned_texts = []
#     print("-------Cleaning Text---------")
#     for text in input_texts:
#         cleaned_text = text.replace("\n", "").replace("\t", "").replace("\r", "")
#         cleaned_text = text.translate(translator).lower()
#         cleaned_texts.append(cleaned_text)
#     # print(text)

#     return cleaned_texts

