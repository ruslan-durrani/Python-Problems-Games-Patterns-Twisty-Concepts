#Vowel words Collector
Para = input("Enter paragraph : ").split()
Vowel = []
for x in Para:
    #for j in x:
    if x[0]=="a" or x[0]=="e" or x[0]=="i" or x[0]=="o" or x[0]=="u":
        Vowel.append(x)
    else:
        pass
print(Vowel)

