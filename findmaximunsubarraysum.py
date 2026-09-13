# 1.brute solution
# num=[1,2,-1,1,3,-1,-5,2,5,-1,3,-4]

# n=len(num)
# max1=0
# for i in range(0,n):
#     total=0
#     for j in range(i,n):
#         total+=num[j]
#         max1=max(total,max1)
# print(max1)

# tc=o(n2)
# sc=0(1)
        
# 2.optimal solution

num=[1,2,1,1,3,-1,-5,2,-1,3,-4]

n=len(num)
max1=0
total=0
for i in range(0,n):
    total+=num[i]
    max1=max(total,max1)
    if(total<0):
        total=0
        
print(max1)

# tc=o(n)
# sc=o(1)


