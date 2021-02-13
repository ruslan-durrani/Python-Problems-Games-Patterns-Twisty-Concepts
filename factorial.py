'''
FACTORIAL
'''
i = 1
factorial = 1
number = int(input("ENter number to find the factorial of :..."))

while i<=number:
    factorial = factorial*i
    i+=1
print("The factorial is :...",factorial)
