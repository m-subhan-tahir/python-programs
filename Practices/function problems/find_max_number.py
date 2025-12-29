def find_max_number(numbers):
    firstItem = numbers[0]
    print(firstItem)
    for i in numbers:
        if firstItem < i:
            firstItem = i
        
    print(f"The largest number of {firstItem}")                
        
        
find_max_number([1,2,30,3,4,5,6,20])        
        