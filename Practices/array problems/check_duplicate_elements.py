# Check Duplicate Element of an Array
# array = [4,5,3,12,3]
# found = False
# for i in range(len(array)):
#     print(i+1)
#     for j in range(i+1,len(array)):
#         if array[i] == array[j]:
#             found = True
#     if found:
#         break    
# print(found)

#Write a program to count duplicate elements from an array
array1 = [10,20,3,4,5,6,7,1,2,3,7,10]
for i in range(len(array1)):
    count = 1
    is_duplicate = False
    #  check if this element appeared before
    for j in range(i):
        if array1[i] == array1[j]:
            is_duplicate = True
            break
        
    #skip already counted elements
    if is_duplicate:
        continue
    
    for k in range(i + 1, len(array1)):
        if array1[i] == array1[k]:
            count += 1
    print(f"{array1[i]} : {count} times")     


    