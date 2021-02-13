import math
a,b,c = eval(input("Enter a b c : "))
disc = b*b - 4*a*c

if disc > 0:
    ABC = math.sqrt(b**2 - 4*a*c)
    root1 = (-b-ABC)/2*a
    root2 = (-b+ABC)/2*a
    print("Roots 1: ",root1)
    print("Roots 2: ",root2)
elif disc == 0:
    ABC = math.sqrt(b**2 - 4*a*c)
    root1 = (-b-ABC)/2*a
    root2 = (-b+ABC)/2*a
    print("Roots 1: ",root1)
    print("Roots 2: ",root2)
else:
    print("no real roots")
