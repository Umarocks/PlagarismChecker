import string
def clean_text(input_texts):
    # Create a translation table to remove punctuation marks
    translator = str.maketrans('', '', string.punctuation)  
    # Remove punctuation marks and convert to lowercase for each string in the array
    cleaned_texts = []
    print("-------Cleaning Text---------")
    for text in input_texts:
        cleaned_text = text.replace("\n", "").replace("\t", "").replace("\r", "")
        cleaned_text = text.translate(translator).lower()
        cleaned_texts.append(cleaned_text)
    
    print(text)

    return cleaned_texts

