# 1.

# num=[1,1,2,3,4,5,4,4,5,6,7,7,8,9,12,10]

# dic={}

# n=len(num)

# for i in range(0,n):
#     dic[num[i]]=0
    
# j=0
# for k in dic:
#     num[j]=k
#     j+=1
          
# print(dic)
# print(num)



# 2

num=[1,1,2,3,4,5,4,4,5,6,7,7,8,9,12,10]
n=len(num)

i=0
j=i+1

while(j<n):
    # print(num)

    if(num[i]!=num[j]):
        i+=1
        num[i],num[j]=num[j],num[i]
    j+=1
    
print(num)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 10, 7, 8, 9, 12, 10]