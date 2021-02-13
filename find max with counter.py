m = 0
count = 1

while True:
    C = int(input("Enter number "))
    if C ==0:
        break
    elif C>m:
        m = C
    elif C<m:
        pass
    elif C == m:
        count +=1
        
print(count,m)
