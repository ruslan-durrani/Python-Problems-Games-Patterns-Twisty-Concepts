for x in range(6):
    print()
    for j in range(0,x):
        print(" * ",end="")
print()
#QUESTION !
for x in range(6):
    print()
    for u in range(6,x,-1):
        print(" ",end="")
    for j in range(0,x):
        print("*",end="")
print()
#QUESTION !
for x in range(6):
    print()
    for u in range(x,6):
        print(" ",end="")
    for j in range(0,x):
        print("*",end=" ")
print()
#QUESTION !
for x in range(6):
    print()
    for j in range(x,6):
        print("*",end=" ")
print()
#QUESTION !
for x in range(6,0,-1):
    print()
    for j in range(x,6):
        print("  ",end="")
    for u in range(0,x):
          print(" *",end="")
#QUESTION !
print()
print()
decr = 7
for x in range(4,0,-1):
    for j in range(x,5):
        print(" ",end="")
    print("*"*decr)
    decr -=2

#Question
for x in range(1,6):
    for j in range(0,x):
        print("*",end=" ")
    print()
for k in range(5,-1,-1):
    for p in range(k,-1,-1):
        print("*",end=" ")
    print()

#Question
for x in range(1,12,2):
    for j in range(0,x):
        print("*",end=" ")
    print()

