'''
Averages
Make a program that asks the user for a series of numbers until
they either want to output the average or quit the program. Extensions: 
1. Expand the program to print the median and mode averages also
2. Include options so that if the user wants to,
they can save their list of numbers to a text file and read them back out
later on.
'''
L1 = []
N = 1
while N !=0:
    N = (int(input("Enter number..:")))
    if N == 0:
        break
    else:
        L1.append(N)
print(L1)
Sum = sum(L1)
print("The average(median) of the list is :.. ",format(Sum/len(L1) , "10.2f"))
x = 0
Num = 0

preC = 0
for j in L1:
    count = 0
    for k in L1:
        if j == k:
            count+=1
        if count>preC:
            
            preC = count
            Num = j
print(Num)
            
            
