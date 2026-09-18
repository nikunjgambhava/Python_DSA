nums=[1,1,2,2,3,3,4,5,7,8,10,14,15]
 
target=6
high = len(nums)-1
low=0
ceil=-1
floor=-1
while(low<=high):
    mid =(low+high)//2
    
    if(nums[mid]==target):
        print("floor and ceil=",nums[mid])
        break
    elif(nums[mid]>target):
        ceil=nums[mid]
        high=mid-1
    else:
        floor=nums[mid]
        low=mid+1
print(ceil,floor)
