'''
Hi this is a program that get a proper list from the user
And then after this program calculate the LCM of each entity
and with the help of self design module called Isprime several prime
factor are calculatedto return a boolian value
'''
def Least(chek):
    from function_prime import Isprime
    i=2
    x = Isprime(chek)
    if x == True:
        return 1
    while i<chek:
        if chek%i==0:
            return i        
        i+=1
    
def main():
    list1 = []
    LCM = []
    for x in range(5):
        nn =(int(input("ENTER A NUMBER :>>> ")))
        list1.append(nn)
        ll = Least(nn)
        LCM.append(ll)
    print("The list:..",list1)
    print("The LCM list.",LCM)
        
main()
