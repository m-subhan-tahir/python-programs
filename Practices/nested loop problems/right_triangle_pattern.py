print("---Right Angle Pattern----")
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()        
    
rows = 4
for k in range(1,rows + 1):
    for l in range(rows - k):
        print(" ", end=" ")
    for m in range(k):
        print("* ",end=" ")
    print()        
    
    