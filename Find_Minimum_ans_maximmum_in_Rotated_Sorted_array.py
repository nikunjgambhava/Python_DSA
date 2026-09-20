
nums=[10,12,14,15,16,2,4,5,6,7,8,9]
l=0
h=len(nums)-1
min1=float("inf")
max1=-1

while(l<=h):
    mid=(l+h)//2
    
    if(nums[mid]<=nums[h]):
        min1=min(min1,nums[mid])
        max1=max(max1,nums[h])
        h=mid-1 
    else:
        min1=min(min1,nums[l])
        max1=max(max1,nums[mid])
        l=mid+1
print(min1)
print(max1)