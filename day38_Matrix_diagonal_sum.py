#38 Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
def diagonalSum(mat):
    pd=0
    sd=0
    n=len(mat)
    for i in range(n):
        for j in range(n):
            if i==j:
                pd+=mat[i][j]
            elif i+j==n-1:
                sd+=mat[i][j]
            else:
                continue
    return pd+sd