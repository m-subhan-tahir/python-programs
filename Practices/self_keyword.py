class CircleAre:
    def __init__(self,r):
        self.r = r
    def  printArea(self):
        a = 3.14 * self.r ** 2 #formula of circle (pir^2)
        return a
ans = CircleAre(6)
print("Area of the Circle is: ",ans.printArea())  
print(ans.__init__(2))    

# Sum of two numbers

class SumOFTwoNumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def print(self):
        sum = self.a + self.b
        return sum
result = SumOFTwoNumbers(10,5)
print(result.print())        

def mes(name):
    return f"Hello {name}!"

def fun1(fun2,name):
    return fun2(name)
#In python We can pass the function as an argument
print(fun1(mes,"Subhan"))



    