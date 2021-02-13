'''
Mastermind
Generate a random four digit number.
The player has to keep inputting four digit numbers until they guess the randomly generated number.
After each unsuccessful try it should say how many numbers they got correct, but not which position they got right.
At the end of the game should congratulate the user and say how many tries it took. Extensions: 
1. Let the user pick an easy mode which shows the user which position that they guessed correctly
2. Let the user pick a hard mode that gives five digits instead of four
3. After the game is finished, ask the user for their name and input their score into a table.
    Show them the high score at the start of the game so that it gives a sense of competition.

'''
import random
Num = random.randint(1000,2000)
String = str(Num)
User_guess = 0
cows = 0
while User_guess != Num:
    if cows == 4:
        print("You Won,")
        break
    cows = 0
    bulls = 0
    User_guess = str(input(" Enter a four digit number "))
    
    
    
    for x in User_guess:
        if x in String:
            Und = String.index(x)
            Index = User_guess.index(x)
            if Und == Index :
                cows+=1
                if Und+1 == 1:
                    print("The correct position is first")
                elif Und+1 == 2:
                    print("The correct position is second")
                elif Und+1 == 3:
                    print("The correct position is third")
                elif Und+1 ==4:
                    print("The correct position is fourth")
    print(cows," cows ",4-cows,"bulls")
                
        
    
