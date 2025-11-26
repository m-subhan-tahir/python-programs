print("-----Square pattern-----")
dims = int(input("Enter the dimensions of square pattern: "))
for i in range(1,dims+1):
    for j in range(1,dims+1):
        print("*",end=" ")
    print()       