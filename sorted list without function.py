#To sort a list without function sort is here
Listdef sort(L1):
    New = []
    for x in range(len(L1)):
        mini = min(L1)
        New.append(mini)
        L1.remove(mini)
    return New
    
LIST = []
for x in range(1,6):
    LIST.append(int(input(str(x)+") Enter number :: ")))
print("The sorted list is :... ",sort(LIST))
