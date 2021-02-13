name = input("What is your name :.. ")
print("Hello, ",name," lets a word guesing game, hangman!..")
Guess = "pak786"
print("The word contains 6 letters:.. ")
print("Start guessing")
correct = 0
counter = 10
while counter!=0:
    Chek = input("Guess character:. ")
    if Chek in Guess:
        print("Correct guess",Chek," found on step ",end=" ")
        point = Guess.index(Chek)
        print("_,"*point,Chek,"_,"*(5-Guess.index(Chek)))
        correct +=1
        if correct ==6:
            break
    else:
        print("Wrong guess:")
        counter-=1
        print("You have " ,counter," more guesses")
   

if correct == 6:
    print("You Guess right :..",Guess)
else:
    print("You couldnt find:. ",Guess)
        
