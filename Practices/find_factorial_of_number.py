print("----- Factorial program ----")
attempt = 0
while True:
    num = int(input("Enter a number to find factorial: "))
    attempt += 1
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        if attempt == 2:
            print("This is your second attempt, please enter a valid number.")
        elif attempt == 3:
            print("This is your last attempt, make it count!")
        elif attempt == 4:
           print("Your attemps has been end. Try again after 1 day.")
           break

    else:
        factorial = 1
        for i in range(1,num+1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}")
        break