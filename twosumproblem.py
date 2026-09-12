# 1

# def sum():
#     nums=[1,3,4,5,6,9,8,12,2]
#     target=13
#     l1=[]
#     n=len(nums)
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             if(nums[i]+nums[j]==target): 
#                 l1.append([i,j])
#     return l1
# print(sum())
        
# 2
nums=[1,3,4,5,6,9,8,12,2]
target=13
n=len(nums)
dic={}

for i in range(0,n):
    r=target-nums[i]
    if(r in dic):
        print([dic[r],i])
        break
    else:
        dic[nums[i]]=i
        