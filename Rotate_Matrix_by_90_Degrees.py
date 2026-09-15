# 1 brute solution

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

n=len(matrix)
# res=[[0 for c in range(n)]for c in range(n)]

# for i in range(n):
#     for j in range(n):
#         res[j][(n-1)-i]=matrix[i][j]
    
# print(res)

# tc=o(n2)
# sc=o(n)


# 2 optimal solution

for i in range(n-1):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
for i in range(n):
    matrix[i].reverse()
print(matrix)

# tc=o(n2)
# sc=o(1)