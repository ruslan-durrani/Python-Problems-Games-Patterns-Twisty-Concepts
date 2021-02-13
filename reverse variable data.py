num = int(input("ENTR number :.."))
X = num
reverse = 0
while num!=0:
    rem = num%10
    new = (reverse*10)+rem
    reverse = new
    num = num//10
print("The reverse of ",X," is ",new)
