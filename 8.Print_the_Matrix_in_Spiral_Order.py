matrix = [[1,2,3,4],
          [12,13,14,5],
          [11,16,15,6],
          [10,9,8,7]]

re=[]

top,left=0,0
bottom=len(matrix)-1
right=len(matrix[0])-1

while(left<=right and top <=bottom):
    for i in range(left,right+1):
        re.append(matrix[top][i])
    top+=1

    for i in range(top,bottom+1):
        re.append(matrix[i][right])
    right-=1

    
    if(left<=right):
        for i in range(right,left-1,-1):
            re.append(matrix[bottom][i])
        bottom-=1

    if(top<=bottom):
        for i in range(bottom,top-1,-1):
            re.append(matrix[i][left])
        left+=1


print(re)