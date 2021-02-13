'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements
of the list that are less than 5.
'''
list1 = []
for x in range(5):
    list1.append(input("NTer number:.. "))
for x in list1:
    if int(x) < 5:
        print(x)
        
