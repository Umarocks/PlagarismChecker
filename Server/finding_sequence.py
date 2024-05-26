def smith_waterman(sequence111, sequence222, match=2, mismatch=-1, gap_penalty=-1):
    words1 = sequence111.split()
    words2 = sequence222.split()

    len_words1 = len(words1)
    len_words2 = len(words2)

    # Initialize the scoring matrix with zeros
    score_matrix = [[0] * (len_words2 + 1) for _ in range(len_words1 + 1)]

    # Initialize variables to keep track of the maximum score and its position
    max_score = 0
    max_i, max_j = 0, 0

    # Fill in the scoring matrix
    for i in range(1, len_words1 + 1):
        for j in range(1, len_words2 + 1):
            if words1[i - 1] == words2[j - 1]:
                diagonal_score = score_matrix[i - 1][j - 1] + match
            else:
                diagonal_score = score_matrix[i - 1][j - 1] + mismatch

            up_score = score_matrix[i - 1][j] + gap_penalty
            left_score = score_matrix[i][j - 1] + gap_penalty

            score_matrix[i][j] = max(0, diagonal_score, up_score, left_score)

            # Update the maximum score and its position
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i, max_j = i, j

    # Traceback to find the alignment
    aligned_words1 = []
    aligned_words2 = []

    i, j = max_i, max_j
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            aligned_words1.insert(0, words1[i - 1])
            aligned_words2.insert(0, '-')
            i -= 1
        elif score_matrix[i][j] == score_matrix[i][j - 1] + gap_penalty:
            aligned_words1.insert(0, '-')
            aligned_words2.insert(0, words2[j - 1])
            j -= 1
        else:
            aligned_words1.insert(0, words1[i - 1])
            aligned_words2.insert(0, words2[j - 1])
            i -= 1
            j -= 1

    # Convert the lists to strings
    aligned_words1 = ' '.join(aligned_words1)
    aligned_words2 = ' '.join(aligned_words2)
    


    return aligned_words1, aligned_words2, max_score

