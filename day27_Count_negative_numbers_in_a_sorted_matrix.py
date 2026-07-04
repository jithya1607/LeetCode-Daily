#27 Count negative numbers in a sorted matrix
# Given a sorted matrix of integers, count the number of negative numbers.
def count_negatives(matrix):
    count = 0
    for row in matrix:
        for num in row:
            if num < 0:
                count += 1
    return count