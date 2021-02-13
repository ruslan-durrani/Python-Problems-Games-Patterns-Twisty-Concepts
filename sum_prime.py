def Isprime(num):
    div = 2
    primi = True
    while div<num:
        if num%div==0:
            primi = False
            break
        else:
            div+=1
    return primi
def main():
    primenumbers = 1
    sum = 2
    i = 3
    print("The prime numbers are :.....")
    print()
    print(sum,end=" ")
    while primenumbers < 20:
        if Isprime(i) == True:
            primenumbers+=1
            print(i,end=",")
            sum+=i
            i+=1
        else:
            i+=1
    print()
    print("The first 20 prime numbers are :...",primenumbers)
    print()
    print("Their Sum is :...",sum)
main()
