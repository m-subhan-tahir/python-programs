print("------------Mini Calculator-------------")
print("Enter the two numbers:")
num1 = int(input())
num2 = int(input())

print("Enter operator that you want to perform calculation on input numbers")
while True:
    ope = input("Enter operator: ")

    if ope == "+":
        print(f"Sum of two numbers is = {num1} + {num2} = {num1 + num2}")
        break

    elif ope == "-":
        print(f"Subtraction of two numbers is = {num1} - {num2} = {num1 - num2}")
        break

    elif ope == "*":
        print(f"Multiplication of two numbers is = {num1} * {num2} = {num1 * num2}")
        break

    elif ope == "/":
        divide = int(num1 / num2)
        print(f"Division of two numbers is = {num1} / {num2} = {divide}")
        break

    else:
        print("Please enter your correct operator")


