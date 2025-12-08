#Count Occurences of a specified array element

def findOccuruence(num):
    array = [1,2,4,5,2,6,4,2,2,2,4,2]
    count = 0
    for i in array:
        if  i == num:
            count+=1
    return count
    
print(findOccuruence(4))            