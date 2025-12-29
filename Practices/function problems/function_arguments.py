
# Positiional Arguments
def fun(*args):
    for val in args:
        print(val)
fun(5,10,15,"afdf")    

#program using Positional Arguments

def findAndSumOfEvenNumbers(*args):
    print("Your List",args)
    sum = 0
    for val in args:
        if val%2 == 0:
            print("Even Numbers from the list",val)
            sum+=val
    print("Sum of Even Numbers = ",sum)        
    
findAndSumOfEvenNumbers(1,2,3,4,5,6,7,8,9,10)    
        
 #Keyword Arguments
# def fun1(**kargs):
#     for k in list(kargs.keys()):
#        if kargs[k] % 2 == 0:
#            print(k)
           
            

# fun1(username="Subhan",age=19,gender="male")                       

# userData = {'username':"Subhan",'age':19,'gender':"male"}

# for key in list(userData.keys()):
#     if userData[key] % 2 == 0:  # Example condition: remove even values
#         del userData[key]
# print(userData)        

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# # Iterate over a list of items
# for key, value in list(my_dict.items()):
#     if value % 2 == 0:
#         my_dict.pop(key)

# print(my_dict)
# # Output: {'a': 1, 'c': 3}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Iterate over a list of the keys
for key in list(my_dict.keys()):
    print(key)
    if my_dict[key] % 2 == 0:  # Example condition: remove even values
        del my_dict[key]

print(my_dict)
# Output: {'a': 1, 'c': 3}

