#"DIce rolling simulator"
import random
print("Lets Roll the dice shayesta....")
Y = "Y"
while Y == "Y":
    num = random.randrange(1,7)
    if num ==1:
        print("--------")
        print("!      !")
        print("!   0  !")
        print("!      !")
        print("--------")
    elif num == 2:
        print("--------")
        print("!      !")
        print("!  00  !")
        print("!      !")
        print("--------")
    elif num == 3:
        print("--------")
        print("!  0   !")
        print("! 0 0 !")
        print("!      !")
        print("--------")
    elif num == 4:
        print("--------")
        print("!  00  !")
        print("!  00  !")
        print("--------")
    elif num == 5:
        print("--------")
        print("!  00  !")
        print("!  00  !")
        print("!   0  !")
        print("--------")
    elif num == 6:
        print("--------")
        print("!  00  !")
        print("!  00  !")
        print("!  00  !")
        print("--------")
    Y = input("Do you want to roll again:.. ").upper()
    
