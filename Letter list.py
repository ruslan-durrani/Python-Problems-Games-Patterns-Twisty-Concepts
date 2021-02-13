'''
Letter list 
Write a program that lets a user choose a letter.
The program will then find all the words beginning
with that letter in a list and print them out.
It should also say how many words it found.
Extensions: 
1. Let the user load up a list of words from a file
   and have the program process them all
2. Change the program so that the user can choose
   whether they want all words with only the start of the letter, or ANY place in the word.
'''
print("List of Words:...............................................")
List = []
Name = input("Enter your name : ").upper()
Items = int(input(Name+" enter the number of items : "))
for x in range(Items):
    List.append(input("Enter Word ").upper())
print(List)
count = 0
Is = "YES"
i = 0

Let = []

Letter = input("Choose a letter to find in the list ").upper()
while True:
    print("Press 1 To desplay all the words starts with ",Letter)
    print("Press 2 To desplay all the words containing the ",Letter,end=": ")
    Choice = int(input())
    if Choice==1 or Choice==2:
        break
    else:
        print("Wrong Input ")
if Choice == 1:
   for x in (List):
       if Letter == x[i]:
           count+=1
           Let.append(x)
elif Choice == 2:
    for j in List:
        if Letter in j:
            count+=1
            Let.append(j)

print("The letter is : ",Letter)
print("Appearnace : ",count)
print("The List is : ",Let)

            
    
