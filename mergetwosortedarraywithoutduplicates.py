n1=[1,2,4,6,8,9,12,34]
n2=[1,2,3,6,7,8,11,12,34,78,90]

n=len(n1)
m=len(n2)
result=[]
i=0
j=0
while(i<n and j<m):
    if(n1[i] <n2[j]): 
        if(len(result)==0 or result[-1]!=n1[i]): 
            result.append(n1[i]) 
        i+=1
    else:
        if(len(result)==0 or result[-1]!=n2[j]): 
            result.append(n2[j]) 
        j+=1

while(i<n):
    if(len(result)==0 or result[-1]!=n1[i]): 
        result.append(n1[i]) 
    i+=1
while(j<m):
    if(len(result)==0 or result[-1]!=n2[j]): 
        result.append(n2[j]) 
    j+=1
    
print(result)
    
