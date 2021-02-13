for x in range(65,70):
    print()
    for j in range(1,6):
        print(chr(x),end=" ")

print()
for x in range(1,6):
    print()
    for j in range(65,70):
        
        print(chr(j),end=" ")
print()
for x in range(1,6):
    print()
    for j in range(69,64,-1):
        print(chr(j),end=" ")

print()
for x in range(69,64,-1):
    print()
    for j in range(1,6):
        print(chr(x),end=" ")
#Question!!

for x in range(65,70):
    print()
    for j in range(65,x+1):
        print(chr(x),end="")
#Question!!
for x in range(65,70):
    print()
    for j in range(65,x+1):
        print(chr(j),end="")
print()
#Question!!
for x in range(70,64,-1):
    print()
    for j in range(65,x+1):
        print(chr(j),end="")
print()
#Question!!
for x in range(70,64,-1):
    print()
    for k in range(65,70):
        print(" ",end="")
        for j in range(65,k):
            print(chr(j),end="")
print()
#Question
N = 65
for x in range(0,5):
    for j in range(x+1,0,-1):
        print(chr(N),end=" ")
        N+=1
    print()
print()
#Question
for x in range(1,6):
    for k in range(6,x,-1):
        print(" ",end=" ")
        
    for j in range(65,65+x,1):
        print(chr(j),end=" ")
    print()


