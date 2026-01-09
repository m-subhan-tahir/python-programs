#example 1:
def fun1():
    print('Hello outer')
    def fun2():
        print("Hello inner")
    fun2()    
fun1() 

#example 2 - Modifying variables using nonlocal variable

def fun3():
    name = "subhan"
    def fun4():
        nonlocal name
        print(name)
        name = "ayan"
        print(name)
    fun4()
    print(name)
fun3()    
        
#example 3 - Access the outer value in inner function

def fun5(a):
    def fun6():
        print(a)
    return fun6 
    
    
closure_fun = fun5(10)  
closure_fun()       

