n_st = int(input("Enter number of students: "))
Max = 0
Smax = 0
for x in range(n_st):
    score = int(input("Enter marks: "))
    if score > Max :
        Smax = Max
        Max = score
    
    if x == n_st:
        break
print("Highest is : ",Max)
print("Second Highest is : ",Smax)
