'''
Password reset program 
Only accept a new password if it is:
1. At least eight characters long
2. Has lower case and upper case letters.
   The password reset program should also make the user input their new password
   twice so that the computer knows that the user has not made any mistakes when
   typing their new password. Extensions: 
1. Make some sort of algorithm to suggest how strong the password is (Weak,
   Medium, Strong) depending on length, whether or not the password has special
   characters in etc

'''
print("__________________PASSWORD RESET PROGRAM____________________")
print()
print("Strong Password includes: Special characters ")
print("                          Symbols ,Numbers ")
print("                          Length of Words")
print()
Store = ""
FF = False
import re
while True:
    Pass = input("Enter Password : ")
    A = True if re.search('[A-Z]',Pass) else False
    B = True if re.search('[a-z]',Pass) else False
    if len(Pass)>=8 and (A==B==True):
        Store = ""+Pass
        num = True if re.search("[0-9]",Pass) else False
        spec = True if re.search("[!,$,%,&,*,£,@,~]",Pass) else False
        L = len(Pass)
        Length = True if L>12 else False
        
        if num==spec==Length==True:
            print("Strong Password")
            final = input("Do you want to final this press OK").upper()
            if final=="OK":
                Store = Pass
                FF = True
                
            else:
                print("Try another ",end=" ")
                continue

        elif num==spec==True or num==Length==True or num==Length==True:
            print("Medium Password. ")
            Med = input("Press OK to final your password or Press no to chnage ").upper()
            if Med=="OK":
                Store = Pass
                FF= True
            else:
                print("Try another ",end=" ")
                continue
        else:
           print("Weak Password. Set another one")
           continue 
    else:
        print("Password must contain atleast 8 characters and upper & lower ase letters")
    if FF == True and Store==Pass:
        count = 3
        while count !=0:
            verify = input("Enter your Password again for verification purposes:.. ")
            if verify==Pass:
                print("Congratulations. Password verified ")
                break
            else:
                count -=1
                print("Attempts left : ",count)
        if verify == Pass:
            break
        else:
            continue
            
            

