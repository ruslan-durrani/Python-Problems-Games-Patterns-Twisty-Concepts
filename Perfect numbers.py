C = 1
while C != 10_000:
    k = 1
    s = 0
    while k<C :
        if C%k==0:
            s += k
        k+=1
    if s == C:
        print(C,end=" ")
    C +=1
    
