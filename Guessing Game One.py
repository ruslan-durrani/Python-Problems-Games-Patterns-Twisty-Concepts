'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
then tell them whether they guessed too low,
too high, or exactly right.
'''
print("Guess The number:................")
import random
ran = random.randint(1,9)
User = int(input("Enter guess:...."))
End = "continue"
while End != "EXIT":
    if ran == User:
        print("You Guess Right:... The number is >.",ran)
        break
    elif User<ran:
        print("You guess too Low:.. ")
    elif User>ran:
        print("You guess too high:...")
    
    End = input("Press any key to continue or press exit ").upper()
    if End !="EXIT":
            User = int(input("Enter guess:...."))
print("Thank for playing>... ")

    
