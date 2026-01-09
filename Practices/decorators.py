def sum(a,b):
    print(a+b)

def smart_sum(func):
    def inner(a,b):
        return func(a,b)
    return inner

result = smart_sum(sum)

result(4,2)

def sum_decorator(func):
    def wrapper(*args):
        print(*args)
        print("Before Execution")
        result = func(*args)
        return result
    return wrapper

@sum_decorator
def add(a,b):
    return a + b

print(add(1,2))
        
    


