'''
Write a program that lets the user input a list of numbers.
Every time they input a new number, the program should give
a message about what the maximum and minimum numbers in the list are.
Extensions 
1. The program should let the user choose the allowable minimum and maximum values,
and should not let the user input something to the list that is outside of these bounds

'''
List1 = []
print("Listing________________________________________")
print()
Name = input("Enter your name :..   ").upper()
ENT = int(input(Name+" enter the number of integer items for the list: "))
for x in range(ENT):
    List1.append(int(input("Enter Data: ")))
minlist = []
maxlist = []
print()
print("New entries......")
print()
new = True
L=True
NewMax = []
NewMin = []
while new:
    N = input("Do you want to add a new number.Or press exit : ").upper()
    if N=="YES":
        NUM = int(input("Enter number to be added: "))
        List1.append(NUM)
        print("The new list is : ",List1)
        for j in range(len(List1)):
            if List1[j]>NUM:
                maxlist.append(List1[j])
            else:
                minlist.append(List1[j])
        print("The list of maximum values is: ",maxlist)
        print("The list of minimum values is: ",minlist)
        select = input("Do you wnat to make changes in MAX list : Press max  ").upper()
        if select == "MAX":
            NewMax = []
            while True:
                allow = int(input(str(maxlist)+" chose the alloweable item or press 0 key to exit "))
                if allow in maxlist:
                    NewMax.append(allow)
                    maxlist.remove(allow)
                elif allow == 0:
                    L = False
                    break
                else:
                    print("This item does not exists in the list : ")
                    print("Choose another item ")
        select = input("Do you wnat to make changes in MIN list : Press min  ").upper()
        if select == "MIN":
            NewMin = []
            for x in range(len(minlist)):
                allow = int(input(str(minlist)+" chose the alloweable item or press 0key to exit: "))
                if allow in minlist:
                    NewMin.append(allow)
                    minlist.remove(allow)
                elif allow == 0:
                    L = False
                    break
                else:
                    print("This item does not exists in the list : ")
                    print("Choose another item ")
        elif select == "ALL":
            print("The original list is : ",List1)
            print("The maximum list is : ",maxlist)
            print("The minimum list is : ",minlist)
            
    if N=="EXIT" and L==False:
       print("The previous list was : ",List1)
       print("The updated List is : ",(NewMax +NewMin))
        
    elif N == "EXIT" or N=="NO":
        new = False
        


