prime_nums = 51
counter = 1
X = True
num = 2
while counter != prime_nums:
    k = 2
    while k < num:
        if num % k == 0:
            X = False
            break
        else:
            X = True
        k +=1
    if X == True:
        print(format(num,"3d"),end=" ")
        if counter % 10 == 0:
            print()
        counter +=1
        
    num += 1
