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
    # Normalize scores (you can use different normalization methods)
    normalized_smith_waterman = smith_waterman_score / max(l1, l2)
    normalized_levenshtein = 1 - (levenshtein_score / max(l1, l2))

    # Combine scores using a weighted average
    # combined_score = (smith_waterman_weight * normalized_smith_waterman +(1 - smith_waterman_weight) * normalized_levenshtein)
    if(len(sequence11)==0):
        return 100;
    combined_score = ((len(sequence11)-levenshtein_score)*100)/len(sequence11)
    # combined_score = ((len(sequence11)-len(alignment2))*100)
    print(len(sequence11))
    return combined_score