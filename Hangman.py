'''
print("Hangman")
guess = "program"
star = ["*" for x in range(7)]
asterisks = ""
stars = "*******"
end = 0
while end != 7:
    n = input(f"(Guess) Enter a letter in word: {str(stars)} ")
    if n in guess:
        for x in range(len(stars)):
            Sind = guess.index(n)
            if guess.index(n) == Sind:
                asterisks += n
            else:
                asterisks += "*"
    print(f"(Guess) this : {str(asterisks)} ")
    break
        
    
'''








print("THE HANGMAN GAME......................................")
print()
print()
Name = input("Enter you name:... ")
print("Let get started...............",Name)
Reserved = "PAK786"
YOUR = []
print("YOU HAVE 10 tries and.... You have to guess 6 letter word..")
print(YOUR)
counter = 6
Attempts = 10
Lcount = 0

while  Attempts != 0:
    Attempts -=1
    User = input("Enter letter :..  ").upper()
    if User in Reserved:
        Index = Reserved.index(User)
        print("You Guess right:.. ,","*"*Index,User,"*"*(5-Lcount))
        YOUR.insert(0,User)
        Lcount+=1
        if Lcount == 6:
            break
        
        counter -=1
        
    else:
        
        print("You have ",Attempts," attempts left ")
    
        
    
if Lcount==6:
    print("You won , you guess right",Reserved)
else:
    print("You Lose")
