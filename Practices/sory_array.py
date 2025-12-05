#algorithm for sort an array
#[12,26,4,64,6,11] 


def numericallySortArray(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
        
numericallySortArray([1,2,3,45,6])        