#getting input of two nums from user:.....
num = int(input("Enter a number :..."))
num1 = int(input("Enter a number :..."))
k = 1
while k<num and k<num1:
    if num%k==0 and num1%k == 0:
        GCD = k
    k+=1
print("The greatest common divisor is ....",GCD)
