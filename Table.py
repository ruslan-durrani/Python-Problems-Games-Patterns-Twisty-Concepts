N = int(input("Enter the table number :.....  "))
for x in range(1,11):
    print(N," x ",format(x,"2d")," = ",format(x*N,"4d"))
print()
#Question
for x in range(1,11):
    print("i =",format(x,"2d"),end=":")
    for j in range(1,11):
        print(format(x*j,"4d"),end=" ")
    print()
    
