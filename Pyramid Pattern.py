for x in range(1,8):
    for h in range(7,x-1,-1):
        print(" ",end=" ")
    for j in range(x,0,-1):
        print(j,end=" ")
    for k in range(1,x+1):
        if k == 1:
            continue
        print(k,end=" ")
    print()
