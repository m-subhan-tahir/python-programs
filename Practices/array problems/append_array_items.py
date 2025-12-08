
def appendArrayItems():
    array = [1,3,5,7,9]
    new_array = array.copy()
    for i in array:
        new_array.append(i)
    return new_array
    
print(appendArrayItems())            