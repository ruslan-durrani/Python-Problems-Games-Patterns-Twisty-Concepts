def even(Q):
    if Q%2==0:
        return True
    else:
        return False
def positive(W):
    if W>0:
        return True
    else:
        return False
def factorial(E):
    F = 1
    i = 1
    for x in range(1,E+1):
        F *= i
        i+=1
    return F
def main():
    num = int(input("Enter number :....."))
    list1 = ["EVEN","POSITIVE","FACTORIAL"]
    print("Enter the number to perform desired task:")
    for x in enumerate(list1):
        print(x)
    k = int(input("Enter choice:,,,"))
    if k == 0:
       EVEN = even(num)
      #EVEN
       if EVEN == True:
          print(num, " is EVEN")
       else:
          print(num," is ODD")
    #Positive
    if  k == 1     :
        Posi = positive(num)
        if Posi == True:
            print(num," is Positive")
        else:
            print(num," is Negative")
    if k==2:
    #factorial
       FAC = factorial(num)
       print("The factorial of ",num," is ",FAC)
main()
