def sortAnArrayinAssendingOrder(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                # swap
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


print("Sort an Assending Order: ",sortAnArrayinAssendingOrder([12, 10, 14, 2,20,15]))

def sortAnArrayinDecendingOrder(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                # swap
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


print("Sort a Decending Order: ",sortAnArrayinDecendingOrder([12, 10, 14, 2,20,15]))
