'''
Email validator 
Make a program to check whether an email address is valid or not. 
For instance, you could make sure that there are no spaces,
that there is an @ symbol and a dot somewhere after it.
Also check the length of the parts at the start, and that the end parts
of the address are not blank. Extensions: 
1. When an email address is found to be invalid, tell the user exactly
   what they did wrong with their email address rather than just saying it is
   invalid
2. Allow the user to choose to give a text file with a list of email
   addresses and have it process them all automatically.
   
'''
'''
    
    elif not("@" in User):
        print("Use @ symobole")
    elif not("." in User):
        print("Use '.' symbol in email "   )
    elif not(User.isnum()):
        print("Include digits")
    else:
        print("Correct")
        break
    User = input("Enter Email.... ")
'''
print("EMAIL Validator:..........   ")
print()
print("The sample address can be :.    example907@example.com")
print()
User = input("Enter you email to validate:..  ")
print()

import re

while True:
    K = True
    x = re.search("[A-Z]",User)
    if  (x):
        print("Start with lower case letters..")
        K = False
    x = re.search("[0-9]",User)
    if not x:
        print("Use digits in between the address")
        K = False
    x = re.search("[%,&,*,$,!,<,>,:,',#,[,],-,_,=,+,]",User)
    if x:
        print("special characters except @ and . are not allowed ")
        K = False
    x = re.search("[@,.]",User)
    if not x:
             print("Use @ symbol and a (.) somewhere after it")
             K = False
    if K ==True:
        print("Email is Valid ")
        break
    
    print("The sample address can be :.    example907@example.com")
    User = input("Enter you email to validate:..  ")
        
        
        
