def linear_search(register, target):
    for i, name in enumerate(register):
        if name == target:
            return i          
    return -1                

register = ["Aman", "Karan", "Riya Desai", "Priya", "Dev"]
idx = linear_search(register, "Riya Desai")
print("Riya Desai present:" , "Yes, seat " + str(idx) if idx != -1 else "No")
