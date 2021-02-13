#common multiple
def main():
    x = int(input("Enter number :....."))
    y = int(input("Enter number :....."))
    i = 1
    count = 0
    C = True
    print("The first 10 common numbers properly \
divisible by :",x," and ",y," are: ")
    while C:
        if (i%x==0 and i%y== 0):
            print(i,end="  ")
            count +=1
        i+=1
        if count == 10:
            C = False
        
main()
