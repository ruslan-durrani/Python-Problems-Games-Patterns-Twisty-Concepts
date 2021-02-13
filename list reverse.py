#reversing a list
'''
firs thing first fill the list ....
'''
L1 = []
num = int(input("Enter the number of Entities: "))
for x in range(1 , num+1):
    L1.append(input(str(x)+")"+" Enter value: "))
print()
#Second thing second using len reverse the list 
print("The reverse List is :......")
for x in range(len(L1)-1,-1,-1):
    print(L1[x])
