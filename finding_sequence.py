# def smith_waterman(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
#     # Initialization
#     rows, cols = len(seq1) + 1, len(seq2) + 1
#     matrix = [[0 for _ in range(cols)] for _ in range(rows)]

#     # Scoring
#     for i in range(1, rows):
#         for j in range(1, cols):
#             match = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
#             delete = matrix[i - 1][j] + gap_penalty
#             insert = matrix[i][j - 1] + gap_penalty
#             matrix[i][j] = max(0, match, delete, insert)

#     # Traceback
#     max_score = 0
#     max_i, max_j = 0, 0

#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][j] > max_score:
#                 max_score = matrix[i][j]
#                 max_i, max_j = i, j

#     # Construct alignment
#     align1, align2 = "", ""
#     i, j = max_i, max_j

#     while matrix[i][j] != 0:
#         if matrix[i][j] == matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
#             align1 = seq1[i - 1] + align1
#             align2 = seq2[j - 1] + align2
#             i -= 1
#             j -= 1
#         elif matrix[i][j] == matrix[i - 1][j] + gap_penalty:
#             align1 = seq1[i - 1] + align1
#             align2 = "-" + align2
#             i -= 1
#         elif matrix[i][j] == matrix[i][j - 1] + gap_penalty:
#             align1 = "-" + align1
#             align2 = seq2[j - 1] + align2
#             j -= 1

#     return align1, align2, max_score


def smith_waterman(sequence1, sequence2, match=2, mismatch=-1, gap_penalty=-1):
    len_seq1 = len(sequence1)
    len_seq2 = len(sequence2)

    # Initialize the scoring matrix with zeros
    score_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    # Initialize variables to keep track of the maximum score and its position
    max_score = 0
    max_i, max_j = 0, 0

    # Fill in the scoring matrix
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
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
    aligned_seq1 = []
    aligned_seq2 = []

    i, j = max_i, max_j
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            aligned_seq1.insert(0, sequence1[i - 1])
            aligned_seq2.insert(0, '-')
            i -= 1
        elif score_matrix[i][j] == score_matrix[i][j - 1] + gap_penalty:
            aligned_seq1.insert(0, '-')
            aligned_seq2.insert(0, sequence2[j - 1])
            j -= 1
        else:
            aligned_seq1.insert(0, sequence1[i - 1])
            aligned_seq2.insert(0, sequence2[j - 1])
            i -= 1
            j -= 1

    # Convert the lists to strings
    aligned_seq1 = ''.join(aligned_seq1)
    aligned_seq2 = ''.join(aligned_seq2)

    return aligned_seq1, aligned_seq2, max_score

