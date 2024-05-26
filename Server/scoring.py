from similarity_compute import levenshtein_distance
from finding_sequence import smith_waterman

def calculate_plagiarism_score(sequence11, sequence22, smith_waterman_weight=0.7):
    # Calculate Smith-Waterman score 
    sequence11=sequence11.strip()
    sequence22=sequence22.strip()
    alignment1, alignment2 ,smith_waterman_score = smith_waterman(sequence11, sequence22)
    print(sequence11)
    print(alignment2)
    # Calculate Levenshtein distance score
    levenshtein_score = levenshtein_distance(sequence11, alignment2)
    l1 = len(sequence11)
    l2 = len(sequence22)
    print(levenshtein_score)
    if(len(sequence11)==0):
        return 100;
    words = sequence11.split()
    combined_score = ((len(words)-levenshtein_score)*100)/len(sequence11)
    combined_score =(((len(words)-levenshtein_score))/len(words))*100;
    print(combined_score, levenshtein_score,len(sequence11), len(words),len(alignment2) )
    return combined_score




# [9.523809523809524, 7.6923076923076925, 9.090909090909092, 5.88235294117647, 6.666666666666667, 15.384615384615385, 22.22222222222222, 80.0, 47.61904761904761, 37.5, 40.0, 100.0, 25.0, 90.9090909090909, 100]