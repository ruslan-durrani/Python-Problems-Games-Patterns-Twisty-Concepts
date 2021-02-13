'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list1 = []
i = 0
L = (a+b)
while i< len(L):
    if  L[i] in L :
        list1.append(L[i])
        L.remove(L[i])
    if L == []:
        break
    i+=1
print("The interction list is :.. ",list1)
