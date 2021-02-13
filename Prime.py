'''
Prime
'''
number = int(input("Enter number to chek its primality: "))
PRIME = True
div = 2
while div<number:
    if number % div == 0:
        PRIME = False
        break
    else:
        div+=1
if PRIME:
    print("PRIME NUMBER")
else:
    print("NON PRIME")
