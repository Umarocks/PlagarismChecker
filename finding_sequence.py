def smith_waterman(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    # Initialization
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Scoring
    for i in range(1, rows):
        for j in range(1, cols):
            match = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = matrix[i - 1][j] + gap_penalty
            insert = matrix[i][j - 1] + gap_penalty
            matrix[i][j] = max(0, match, delete, insert)

    # Traceback
    max_score = 0
    max_i, max_j = 0, 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j

    # Construct alignment
    align1, align2 = "", ""
    i, j = max_i, max_j

    while matrix[i][j] != 0:
        if matrix[i][j] == matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i - 1][j] + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        elif matrix[i][j] == matrix[i][j - 1] + gap_penalty:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return align1, align2, max_score