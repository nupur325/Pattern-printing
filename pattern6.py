for i in range(1,6): #i represents number of rows
    for j in range(5-i): #space printing before star
        print(" ",end=" ")
    for k in range(i): #print stars with i value 
        print("*",end=" ")
    print() #print return to i loop