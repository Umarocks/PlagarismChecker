def levenshtein_distance(str1, str2):
    words1 = str1.split()
    words2 = str2.split()
    # Create a matrix to store distances
    matrix = [[0] * (len(words2) + 1) for _ in range(len(words1) + 1)]
    # Initialize the matrix
    for i in range(len(words1) + 1):
        matrix[i][0] = i
    for j in range(len(words2) + 1):
        matrix[0][j] = j
    # Fill the matrix
    for i in range(1, len(words1) + 1):
        for j in range(1, len(words2) + 1):
            cost = 0 if words1[i - 1] == words2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )
    # Return the Levenshtein distance at the word level
    return matrix[len(words1)][len(words2)]
