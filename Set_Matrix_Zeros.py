# 1

matrix = [[1,23,4,12],
          [65,78,0,34],
          [56,0,3,23],
          [12,23,3,4]]

# def markinfinity(matrix, r, c):
#     n = len(matrix)
#     m = len(matrix[0])
    
#     # column mark
#     for i in range(n):s
#         if matrix[i][c] != 0:
#             matrix[i][c] = float("inf")
    
#     # row mark
#     for j in range(m):
#         if matrix[r][j] != 0:
#             matrix[r][j] = float("inf")

# def setzero(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
    
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 markinfinity(matrix, i, j)
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == float("inf"):
#                 matrix[i][j]=0
#     return matrix
# print(setzero(matrix))

# 2.

def setzero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    row = [0 for c in range(n)]
    col = [0 for v in range(m)]
    
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = -1
                col[j] = -1
    
    for i in range(n):
        for j in range(m):
            if row[i]==-1 or col[j]==-1:
                matrix[i][j] = 0
    return matrix

print(setzero(matrix))