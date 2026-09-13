# 1 brute solution

stock=[7,4,5,2,3,1,8,9,4]

n=len(stock)
# maxp=0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if(stock[i] < stock[j]):
#             total=stock[j]-stock[i]
#             maxp=max(maxp,total)
# print(maxp)

# tc=o(n2)
# sp=O(1)

#2 optimal solution

maxp=0
minp=float("inf")

for i in range(0,n):
        minp=min(minp,stock[i])
        maxp=max(maxp,stock[i]-minp)
print(maxp)

# tc=o(n)
# sp=o(1)
