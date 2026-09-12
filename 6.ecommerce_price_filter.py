prices = [10000, 25000, 40000, 48000, 50000, 52000, 60000]
target = 50000

low = 0
high = len(prices) - 1
answer = -1   
while low <= high:
    mid = (low + high) // 2
    
    if prices[mid] >= target:
        answer = mid      
        high = mid - 1    
    else:
        low = mid + 1     

if answer != -1:
    print("First product >= target:", prices[answer])
else:
    print("No product found")
