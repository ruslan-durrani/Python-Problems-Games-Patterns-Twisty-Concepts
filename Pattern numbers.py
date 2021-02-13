for x in range(10):
    print()
    for j in range(0,x):
        print(x,end="")
#Question!!
for x in range(1,10):
    print()
    for j in range(1,x):
        print(j,end="")
#Question!!!
for x in range(10):
    for j in range(x,10):
        print(" ",end="")
    for k in range(1,x+1):
        print(k,end="")
    print()
#Question!!!
for x in range(10):
    for j in range(x,10):
        print(" ",end="")
    for k in range(1,x+1):
        print(x,end="")
    print()
#Questiom
print()

for x in range(5,-1,-1):
    for j in range(x,0,-1):
        print(j,end=" ")
    print()
print()
#Question
'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
for x in range(0,6):
    for j in range(5,x,-1):
        print(j,end=" ")
    print()
#Question
print()
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
for x in range(0,6):
    for j in range(1,x+1):
        print(j,end=" ")
    print()

for x in range(5,1,-1):
    for j in range(1,x):
        print(j,end=" ")
    print()

#Question
for x in range(1,4):
    print(x,end=" ")
    if x == 2:
        for j in range(2,x+1,2):
            print(j+2,end=" ")
    if x == 3:
        for h in range(3,x+6,3):
            print(h+3,end=" ")
    print()
for l in range(2,0,-1):
    print(l,end=" ")
    if l == 2:
        for g in range(2,l+1,2):
            print(g+2,end=" ")
    print()
'''
1 
2 4 
3 6 9 
2 4 
1
'''

#question
def pt(n):
    for x in range(1,n+1):
        print()
        for j in range(n,x,-1):
            print(" ",end=" ")
        for k in range(x,0,-1):
            print(k,end=" ")
N = int(input("Enter number : "))
pt(N)
