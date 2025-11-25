print("Multiplication table")
num = int(input("Enter your table number: "))
sum = 0
for i in range(1,11):
    print(f"{num} * {i} = {i * num}")
    sum += (i*num)
print(f"\nSum of {num} * 1...10 = {sum}")    