# array = [1,2,3,4,5]
# res = map(int,array)
# print(list(res))

# #map with lambda
# array1 = [1,2,3,4,5]
# result1 = list(map(lambda x: x **2,array1))
# print(result1)

# #map with multiple iterables

# array2 = [2,3,4,5]
# array3 = [1,3,6,8]
# result2 = list(map(lambda a,b: a + b, array2,array3))

# print(result2)


# array4 = ["subhan","Subhan","Ayan"]

# # result3 = list(map(lambda name: name.upper(), array4))
# # print(result3)
# result3 = list(map(str.upper,array4))
# print(result3)
# for name in result3:
#     print(name)

#extract uppercase letter from a list
#long method
array6 = ["Subhan","Hashir","bAnana","manGo"]
# uppercaseletters = []
# def checkUppercaseLetter(array6):
#     for word in array6:
#         for char in word:
#             if char.isupper():
#                 uppercaseletters.append(char)
#     return uppercaseletters            
# result_uppercase_letters = checkUppercaseLetter(array6)    
# print(result_uppercase_letters)


#short method
uppercase_letters = filter(lambda char: char.isupper(),''.join(array6))
print(list(uppercase_letters))

