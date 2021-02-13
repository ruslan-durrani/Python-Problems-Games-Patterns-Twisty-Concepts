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
