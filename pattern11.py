for i in range(5):
    print('  '*(5-i+1),end="") # pyramid logic
    for j in range(2*i+1):
        if (j==0 or j==2*i or i==5-1): 
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()