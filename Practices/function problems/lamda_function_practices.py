helloworld = lambda a,b,c :  a + b + c
print(helloworld(1,2,3))

# write the program for checking number positive or negative

checkNumber = lambda  num : "Positive" if num > 0 else "negative"

print(checkNumber(-1)) 
print(checkNumber(2)) 

li =  [lambda arg=x: arg * 10 for x in range(1,5)]

for i in li:
    print(i())