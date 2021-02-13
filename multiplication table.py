print(format("Multiplication Table",">40s"),"\n")
print(" \t",end="")
for x in range(1,11):
    print(format(x,"3d"),end=" ")
print()
for x in range(60):
    print("-",end="")
print()
for x in range(1,11):
    print(format(x,"2d"),"|","\t",end="")
    for j in range(1,11):
        print(format(j*x,"3d"),end=" ")
    print()
