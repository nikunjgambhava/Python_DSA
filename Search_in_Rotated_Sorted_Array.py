nums=[10,12,14,15,2,4,5,6,7,8,9]
target=15


# 1 brute solutution

# def ser(nums,target):
#     for i in range(len(nums)):
#         if(target==nums[i]):
#             return i
#     return "NOT FOUND"
# print(ser(nums,target))
    
    
# 2

def ser2(nums,target):
    l=0
    h=len(nums)-1

    while(l<=h):
        mid =(l+h)//2
        if(nums[mid]==target):
            return mid
        if(nums[mid]<=nums[h]):
            if(nums[mid]<=target<=nums[h]):
                l=mid+1
            else:
                h=mid-1
        else:
            if(nums[l]<=target<=nums[mid]):
                h=mid-1
            else:
                l=mid+1
    return "not found"
            
print(ser2(nums, target))

        