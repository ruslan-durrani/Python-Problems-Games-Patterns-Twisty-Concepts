a,b,c = eval(input("Eter numbers: "))
if b<a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif a<b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)
elif a<c>b:
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)
