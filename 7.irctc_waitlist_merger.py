list1 = [2, 5, 9, 14, 20]
list2 = [1, 4, 8, 15, 18]

merged = []
i = 0   
j = 0   
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i = i + 1
    else:
        merged.append(list2[j])
        j = j + 1

while i < len(list1):
    merged.append(list1[i])
    i = i + 1

while j < len(list2):
    merged.append(list2[j])
    j = j + 1

print("Final merged list:", merged)
