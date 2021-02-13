#palindrom string ........
Str = input("Enter a string:..").upper()
length = len(Str)
x = True
i = 0
while i<length :
    if Str[i] == Str[length-1]:
        x = True
        i+=1
        length-=1
    else:
        x = False
        break
    
        
if x:
    print("Palindrome")
else:
    print("NON- Palindrome")
