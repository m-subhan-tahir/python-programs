print("Multiplication table")
num = int(input("Enter your table number: "))
endNum = int(input("Enter your ending number: "))
sum = 0
for i in range(1,endNum+1):
    print(f"{num} * {i} = {i * num}")
    sum += (i*num)
print(f"\nSum of {num} * 1...10 = {sum}")    