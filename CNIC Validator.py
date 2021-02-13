Cnic = "*****-*******-*"
X = "NO"
while X != "YES":
    ID = input(f"Enter your Cnic {Cnic} : ")
    if "-" in ID:
        if len(ID) != 15:
            print("Numbers are missing")
            continue
    else:
        if len(ID) != 13:
            print("Numbers are missing")
            continue
    if Cnic[5]==ID[5] and Cnic[-2] == ID[-2]:
        print("Pattern Correct")
        X = input("Are the numbers correct: ").upper()
    elif "-" not in ID:
        ID = list(ID)
        ID.insert(5, "-")
        ID.insert(-1,"-")
        S = ""
        for x in ID :
            S += x
        X = input(f'Is this pattern {S} correct: ').upper()
        
