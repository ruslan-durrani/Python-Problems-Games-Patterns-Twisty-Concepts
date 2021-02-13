'''
Basic lists 
Make a program that lets a user input a series of names into a list.
The program should then ask the user whether they want to print out the list in the original order,  or in reverse.
Extensions: 
1. Enable the user to choose what number item in the list they want to print out
2. Enable the user to only print out a ‘slice’ of the list (eg item three to item nine only)
3. Enable the user to remove any items of the list that they want to

'''
Name = input("Enter your name: ")
List1 = []
items = int(input(Name+" enter the number of Items:... "))
print("Naming list Entry:.._______________________________________")
for x in range(items):
    List1.append(input(str(x+1)+") input : ").upper())
Re = input(Name+" press R to print the list in reverse order or press any key ").upper()
if Re=="R":
    print(List1[::-1])
else:
    print(List1)
print()
EX = "Shayesta"
while EX != "NO":
    print()
    print("OPERATIONS____________________________")
    Choices = ["Do you want to select an item: ","Dispay specific sequence of items","Do you want to remove an item"]
    for k in enumerate(Choices):
        print(k)
    CH = int(input("Choose operation by pressing the numbers:.. "))
    if CH==0:
        IN = int(input("Enter the number of the item: "))
        print("The item you were looking for : ",List1[IN])
        contin = input("Press Yes, if you want to want to make another operation ").upper()
        if contin== "YES":
            continue
        else:
            EX = "NO"
    elif CH == 1:
        L = int(input("The squence starts from : "))
        R = int(input("The squence ends with : "))
        print("The sequence is : ",List1[L:R+1])
        contin = input("Press Yes, if you want to want to make another operation ").upper()
        if contin== "YES":
            continue
        else:
            EX = "NO"
    elif CH==2:
        IN = (input("Enter the entity you want to remove: ")).upper()
        List1.remove(IN)
        contin = input("Press Yes, if you want to want to make another operation ").upper()
        if contin== "YES":
            continue
        else:
            EX = "NO"
    else:
        print("Wrong input. Try again")
        
    


