from similarity_compute import levenshtein_distance
from finding_sequence import smith_waterman

def calculate_plagiarism_score(sequence1, sequence2, smith_waterman_weight=0.7):
    # Calculate Smith-Waterman score
    alignment1, alignment2 ,smith_waterman_score = smith_waterman(sequence1, sequence2)
    print(alignment1)
    print(alignment2)
    # Calculate Levenshtein distance score
    levenshtein_score = levenshtein_distance(sequence1, alignment2)
    l1 = len(sequence1)
    l2 = len(sequence2)
    # Normalize scores (you can use different normalization methods)
    normalized_smith_waterman = smith_waterman_score / max(l1, l2)
    normalized_levenshtein = 1 - (levenshtein_score / max(l1, l2))

    # Combine scores using a weighted average
    combined_score = (smith_waterman_weight * normalized_smith_waterman +(1 - smith_waterman_weight) * normalized_levenshtein)

    return combined_score