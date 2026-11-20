n = 5 #initialize n = 5 as we will print in 5 rows and column
for i in range(1, n+1):  # Controls rows from 1 to 5

    for j in range(i):  # print from row 1
        print("*", end=" ")
    for j in range(2*(n-i)):  # Prints spaces in the middle
        print(" ", end=" ")
    for j in range(i):  # Prints stars on the right side
        print("*", end=" ")
    print()  # moves to i loop

for i in range(n-1, 0, -1):  # row printind loop... start from reverse printing
    for j in range(i):  # print from left side of the program
        print("*", end=" ")
    for j in range(2*(n-i)):  # space print from left 
        print(" ", end=" ")
    for j in range(i):  # print from right side of code
        print("*", end=" ")
    print()   # moves to i loop
