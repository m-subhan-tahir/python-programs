# from functools import reduce
# import operator
# subject_marks = [('English',98),('Maths',90),('Chemistry',97)]
# print(subject_marks.sort(key=lambda x: x[1]))
# print(subject_marks)

# #reduce-method

# def sum(x,y):
#     return x + y

# a = [1,2,3,4,5]

# res = reduce(sum,a)
# print(res)
    
# #using reduce with lambda function

# res1 = reduce(lambda x,y:x * y ,a)

# print(res1)

# a1 = [2,4,6,8,10]
# print(reduce(operator.add,a1))
# print(reduce(operator.mul,a1))

# print(reduce(operator.add,[1,2,3]))

#filter-method

def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b)) # Convert filter object to a list

fruits = ['apple','guava','watermilon','Avocado']
new_Array = []
def start_a(w):
    return w.lower().startswith('a')
def lowerFirstLetter(fruits):
    for i in fruits:
        item = i.lower()
        new_Array.append(item)

lowerFirstLetter(fruits)        
    
result = filter(start_a,new_Array)
print(list(result))