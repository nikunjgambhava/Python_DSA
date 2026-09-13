# 1.brute solution 

nums=[4,5,-2,10,-3,-10]
# p=[]
# n=[]
# for i in range(0,len(nums)):
#     if(nums[i]>=0):
#         p.append(nums[i])
#     else:
#         n.append(nums[i])
# for i in range(0,len(nums)//2):
#     nums[i*2]=p[i]
#     nums[(i*2)+1]=n[i]
    
# print(nums)

# tc=o(n+n/2) 
# sc=o(n/2+n/2) =o(n)

# 2.optimal solution

n1=len(nums)

re=[0]*n1
p,n=0,1
for i in range(0,n1):
    if(nums[i]>=0):
        re[p]=nums[i]
        p+=2
    else:
        re[n]=nums[i]
        n+=2
print(re)

# tc = o(n)
# sc = o(1)