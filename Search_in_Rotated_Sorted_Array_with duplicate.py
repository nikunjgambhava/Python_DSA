#dulpicate array
nums=[7,7,7,7,7,7,7,1,2,3,4,5,6,7]
target=1
def ser(nums,target):
    l=0
    h=len(nums)-1

    while(l<=h):
        mid =(l+h)//2
        if(nums[mid]==target):
            return "found"
        if(nums[l]==nums[mid]==nums[h]):
            l+=1
            h-=1
            continue
        
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
            
print(ser(nums, target))