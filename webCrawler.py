import gensim
from gensim import corpora
from gensim import similarities
import nltk
from fetch_url import get_url
from parsing import parse_url
from string_preprocessing import string_cleaning
from similarity_compute import levenshtein_distance
from finding_sequence import smith_waterman
from filtering import preprocessing
from array import array
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from scoring import calculate_plagiarism_score



def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stopwords and lowercase the words
    # stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() ]
    return set(filtered_words)

def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0


query = []
urls = [
"https://lua-api.factorio.com/latest/","https://fabricmc.net/wiki/tutorial:mixin_injects","https://leetcode.com/problems/sort-vowels-in-a-string" ]

reference_documents=[]
sentences = []
score_tracker=0
scoree = []

# Example
sequence1 = "Given a 0-indexed string s, permute s to get a new string t such that:All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i]. Mixin InjectsIntroduction Injects allows you to place custom code at a specified position inside an existing method. For a working example, view the Practical Example category at the bottom of this page. The standard form of an inject is as shown: This site contains the reference documentation for creating Factorio mods, as well as a few auxiliary topics. Mods can modify gameplay in a variety of ways, such as adding new machines or showing informative GUIs. They are distributed via the mod portal, making them accessible through the in-game mod manager. The API is split into three distinct parts: The settings, prototype, and runtime stages, which are introduced in more detail below. Mods go through these stages in a specific way, which is known as the Data Lifecycle. Understanding it is essential to writing a properly working mod. Mods are written in Lua 5.2, and need to follow a certain structure. A tutorial-based introduction to modding can be found on the wiki. "
#sequence2 = "If you’re reading this in the US or Canada, you’re likely familiar with the sport of soccer. But, if you’re reading this pretty much anywhere else, then you probably know the same game rules and call it football. What’s the difference?How did we end up with two names, football and soccer, for the same sport?Let’s start in England in the 1800s. Young men, especially at boarding schools, played a number of versions of moving a ball (with hands or feet) across an opponent’s goal. At Rugby School, for instance, they played a version that allowed for use of the hands; at Eton College, only feet were permitted.So, in 1863 in London, a Football Association (the world’s first) was formed to standardize the rules. Two codes resulted from it: rugby football, after Rugby School, and association football, after that newly formed association.Keep Learning New Words Every Day!Get the Word of The Day delivered straight to your inbox!yourname@email.comWhere does the word soccer come from?Now, around the 1870s, students, especially at Oxford University, were fond of a playful slang practice where they shortened words and added –er to their end. Breakfast, for instant, became brekker. Rugby? Rugger. Football? Footer.The association in association football was also shortened to soccer. This clips off the first and last three syllables of association, leaving –soc-, onto which that chummy –er was added, yielding soccer. The term is first recorded as socker in 1891. Footer is slightly older, found in that fateful year of 1863.What is the origin of American football?But, what about that other football that people in the US bring to the Super Bowl? American football (a term recorded in the 1870s) is based on rugby and had already taken off by the time association football became popular in the US.For whatever reason, the name soccer stuck for association football and football for the gridiron sport. In fact, the governing body for soccer in the US was called the United States Soccer Football Association until 1974.How many football fans know the origins of the terms used in the American sport? Learn about quarterback and more, here.Does anyone else around the world call football soccer?Americans and Canadians aren’t alone, however, in calling the sport soccer. Many in Australia, New Zealand, and Ireland call association football soccer, likely as a way to distinguish it from Australian rules football and Gaelic football, which are commonly referred to just as football in those places—just as Americans call American football simply football.So, the next time a British person thumbs their nose at you for calling football soccer, you can let them know that soccer was a UK original! And, if you’re having trouble keeping all these names straight, take a page from Spanish and call it … fútbol!"
sequence1 = preprocessing(sequence1)
# print(sequence1)
plag=0;
# get_url(urls,sequence1) 


sequence1 = sequence1.split('.')
sequence1_dup = sequence1
print(sequence1)
print(len(sequence1))
# we can do one thing that is to get 2 url for each sentence divided by "." this will help optimize 
# as right now we are comparing all substr of seq1 with url of substr[i]
for url in urls:  
    sequence2=['factorio api docs version ', '', 'this site contains the reference documentation for creating factorio mods, as well as a few auxiliary topics', ' mods can modify gameplay in a variety of ways, such as adding new machines or showing informative guis', ' they are distributed via the mod portal, making them accessible through the in-game mod manager', ' the api is split into three distinct parts: the settings, prototype, and runtime stages, which are introduced in more detail below', ' mods go through these stages in a specific way, which is known as the data lifecycle', ' understanding it is essential to writing a properly working mod', ' mods are written in lua ', ', and need to follow a certain structure', ' a tutorial-based introduction to modding can be found on the wiki', ' settings stage - settingsthe settings stage takes place during game start-up, allowing mods to define the setting prototypes they need', ' their documentation is found on the wiki', ' prototype stage - datathe prototype stage takes place during game start-up as well, with the goal of providing the game with prototypes, which are the templates for crafting machines, recipes, and more', ' runtime stage - controlthe runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', 'the api is split into three distinct parts: the settings, prototype, and runtime stages, which are introduced in more detail below', ' mods go through these stages in a specific way, which is known as the data lifecycle', ' understanding it is essential to writing a properly working mod', ' mods are written in lua ', ', and need to follow a certain structure', ' a tutorial-based introduction to modding can be found on the wiki', ' settings stage - settingsthe settings stage takes place during game start-up, allowing mods to define the setting prototypes they need', ' their documentation is found on the wiki', ' prototype stage - datathe prototype stage takes place during game start-up as well, with the goal of providing the game with prototypes, which are the templates for crafting machines, recipes, and more', ' runtime stage - controlthe runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', 'mods are written in lua ', ', and need to follow a certain structure', ' a tutorial-based introduction to modding can be found on the wiki', ' settings stage - settingsthe settings stage takes place during game start-up, allowing mods to define the setting prototypes they need', ' their documentation is found on the wiki', ' prototype stage - datathe prototype stage takes place during game start-up as well, with the goal of providing the game with prototypes, which are the templates for crafting machines, recipes, and more', ' runtime stage - controlthe runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', 'the settings stage takes place during game start-up, allowing mods to define the setting prototypes they need', ' their documentation is found on the wiki', ' prototype stage - datathe prototype stage takes place during game start-up as well, with the goal of providing the game with prototypes, which are the templates for crafting machines, recipes, and more', ' runtime stage - controlthe runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', 'the prototype stage takes place during game start-up as well, with the goal of providing the game with prototypes, which are the templates for crafting machines, recipes, and more', ' runtime stage - controlthe runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', 'the runtime stage takes place alongside normal gameplay, and allows interaction with the game world in a number of ways', ' it is based on events being fired for mods to react to, with the api functionality being provided via objects of various classes', '']

    # sequence2=string_cleaning(url,sequence2)
    
    print("----------------------PRINTING S2-------------------------------")
    # print(sequence2)
    
    # sequence2 = preprocessing(sequence2)
    # sequence2 = sequence2.split('.')
    print(sequence2)  
    for sequence in sequence1:
        if(len(sequence1)>len(scoree)):
            scoree.append(0.0)
            # print("........................................")
            alignment1,alignment2,score = smith_waterman(sequence, sequence2)
            final_score = calculate_plagiarism_score(sequence1,alignment2)
            scoree[score_tracker]=max(scoree[score_tracker],score)
            # print("Sequence 1:", alignment1)
            # print("Sequence 2:", alignment2)
            # print("Alignment Score:", score) 

            # distance = levenshtein_distance(sequence, alignment2)
            # # print(f"Levenshtein Distance between '{sequence}' and '{alignment2}': {distance}")  
            # a = (len(alignment2)-distance)
            
            # if(a>0):
            #     print("JACCARD")
            #     str1 = preprocess_text(sequence)
            #     str2 = preprocess_text(alignment2)
            #     # similarity = jaccard_similarity(str1,str2)
            #     similarity = a
            #     if(scoree[score_tracker]<similarity and len(alignment2)>10):
            #         scoree[score_tracker]=similarity
            #     print("........................................")
            #     print("aln 1:", alignment1)
            #     print("aln 2:", alignment2)
            #     print("Alignment Score:", score) 
            #     print(f"Levenshtein Distance between '{sequence}' and '{alignment2}': {distance}")  
            #     print("Umaryabou")
            #     print(scoree[score_tracker])
                
                # print("........................................")
        
    score_tracker+=1
print(sentences)
print("Final Plagarism Score ------" )
print(plag) 
print(scoree)
plagiarism_score = (sum(scoree)/len(scoree))*100
print( f"{plagiarism_score}%")


