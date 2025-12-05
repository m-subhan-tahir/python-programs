# Write the algorithm of checkboard pattern.
# step 1:create a outer loop for print the rows. /done
# step 2:Inside each row make the columns using inner loop
# werwer 3:print the X and make third loop for print O 4 divided by 2



# rows = 5
# columns = 5
# for i in range(rows):
#     for j in range(columns):
#         if (i + j) % 2 == 0:
#             print("X",end=" ")
#         else:
#             print("O",end=" ")   
#     print()         
            
                  
 # Make the program print the no of rows and columns from the user input
 
# userRows = int(input("Enter no of rows: "))                                                                                                                                                                                                                                     
# userColumns = int(input("Enter no of columns: ")) 
 
# for k in range(1,userRows+1):
#     print(f"Row {k}:",end=" ")
#     for l in range(1,userColumns+1):
#         print(f"Column {l}", end=" ")
#     print()        
 
# print coordinates using nested loop
for m in range(1,4):
    for n in range(1,4):
        print(f"({m},{n})",end=" ")
    print()                        
                                                                                                                                                                                                                        