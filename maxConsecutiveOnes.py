num=[1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1]

count=0
max_count=0

for i in range(0,len(num)):
    if(num[i]==1):
        count+=1
    else:
        max_count=max(count,max_count)
        count=0
        
result=max(count,max_count)
print(result)