# 1

nums=[1,1,2,3,3,3,3,3,3,4,4,5,5,6,6,7,7,8,9,10]
target=3

# f=-1
# l=-1
# for i in range(len(nums)):
#     if target==nums[i]:
#         if f==-1: 
#             f=i
#         l=i
# print(f,l)


# 2
def lowerbound(nums,target):
    low=0
    high=len(nums)-1
    l=-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            l=mid
            high=mid-1
        else:
            low =mid+1
    return l
    
def upperbound(nums,target):
    low=0
    high=len(nums)-1
    h=-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>target):
            h=mid
            high=mid-1
        else:
            low =mid+1
    return h-1
print(lowerbound(nums,target))

print(upperbound(nums,target))