# 1
num=[0,2,3,4,5,6,7,9,10,8]

# n=len(num)

# for i in range(0,n):
#     if i not in num:
#         print(i)
        
# 2

# dic={}

# for i in range(0,len(num)+1):
#     dic[i]=0
# for n in num:
#     dic[n]=1
        
# for a,b in dic.items():
#     if(b==0):
#         print(a)
# print(dic)

s=sum(num)
n=len(num)

re=(n*(n+1)//2)-s
print(re)
   


git remote add origin https://github.com/nikunjgambhava/Python_DSA.git
