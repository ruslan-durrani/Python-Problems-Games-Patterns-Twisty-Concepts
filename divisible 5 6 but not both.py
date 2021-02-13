P = 0
for x in range(100,1001):
    if (x%5==0 or x%6==0)and not(x%5==0 and x%6 == 0):
        print(x,end=" ")
        P +=1
        if P%10==0:
            print()
        
        
