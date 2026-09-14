# 1. brute solution
num=[1,1,2,4,5,99,101,98,100,6]

n=len(num)

# maxc=0

# for i in range(n):
#     m=num[i]
#     cnt=1
#     while(m+1 in num):
#             cnt+=1
#             m=m+1
#     maxc=max(maxc,cnt)
    
# print(maxc)
        
# 2 batter

# maxc=0
# count=0
# lastsmall=0
# num.sort()
# for i in range(n):
#     m=num[i]
#     if(m-1==lastsmall):
#         count+=1
#         lastsmall=m
#     elif(m!=lastsmall):
#         count=1
#         lastsmall=m
        
#     maxc=max(maxc,count)
# print(maxc)
        
# 3 optimal

my_set=set()

for i in range(n):
    my_set.add(num[i])
longest=0
for m in my_set:
    if(m-1 not in my_set): 
        x=m
        count=1
        while(x+1 in my_set):
            count+=1
            x+=1
        longest=max(longest,count)
    
print(longest)


