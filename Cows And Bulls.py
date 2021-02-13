'''
Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place,
they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls”
they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and
tell the user at the end.
'''
import random
Num = random.randint(10,20)
String = str(Num)
User_guess = 0
cows = 0
bulls = 0
while User_guess != Num:
    User_guess = str(input(" Guess number between 10-20 "))
    
    if User_guess == String and cows == 2:
        print("You Won,")
        break
    else:
        for x in User_guess:
            if x in String:
                Und = String.index(x)
                Index = User_guess.index(x)
                if Und == Index :
                    cows+=1
        print(cows," cows ",2-cows,"bulls")
    cows = 0
    bulls = 0
        
    
