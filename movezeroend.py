# 1.brute

nums=[1,2,0,3,5,0,6,0,3,5,6]

# n=len(nums)
# temp=[]
# nz=len(temp)
# print(nums)
# for i in range(0,n):
#     if(nums[i]!=0):
#         temp.append(nums[i])
# nz=len(temp)
# for i in range(0,nz):
#     nums[i]=temp[i]

# for i in range(nz,n):
#     nums[i]=0
        
        
# print(temp)
# print(nums)
# print(nz)
nums=[1,2,0,3,5,0,6,0,3,5,6]
n=len(nums)

i=0

while(i < n):
    if(nums[i]==0):
        break
    i+=1
j=i+1
while(j<n):
    if(nums[j]!=0):
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1

print(nums)
