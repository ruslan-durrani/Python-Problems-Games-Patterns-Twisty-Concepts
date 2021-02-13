print("\n******************** Snake|Water|Gun **********************")
print("\nRules:\n1)Snake can drink water\n2)Water can Swallow Gun\n3)Gun can destroy Snake\n")
Play ="YES"
Count = 0
while Play != "NO":
    Count +=1
    import random
    C = random.randint(1,3)
    if C==1:
        Comp="S"
    elif C==2:
        Comp="W"
    else:
        Comp ="G"
    
    User = input("\nYour turn: slect Snake(s) Water(w) or Gun(g) ").upper()
    if Comp == User:
        print(f"\nYou {User} Computer {Comp} : Match Tie \n")
    elif Comp == "S":
        if User =="W":
            print(f"\nYou Water & Computer Snake:  Computer Won\n")
        elif User =="G":
            print(f"\nYou Gun & Computer Snake:  You Won\n")
    elif Comp == "W":
        if User =="S":
            print(f"\nYou Snake & Computer Water:  You Won\n")
        elif User =="G":
            print(f"\nYou Gun & Computer Water:  Computer Won\n")
    elif Comp == "G":
        if User =="W":
            print(f"\nYou Water & Computer Gun:  You Won\n")
        elif User =="S":
            print(f"\nYou Snake & Computer Gun:  Computer Won\n")
    else:
        print("\nWrong Input \n")
    if Count == 3:
        Play = input("\nDo you want to play again? Yes/No ").upper()
