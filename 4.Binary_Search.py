def binary_search(words, target):
    low, high = 0, len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1      
    return -1

dictionary = ["Apple", "Book", "Cat", "Dog","Fox", "Gate"]
idx = binary_search(dictionary, "Dog")
print("Found at index:", idx)
